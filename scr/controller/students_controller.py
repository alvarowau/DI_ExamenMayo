from PySide6.QtWidgets import QAbstractItemView, QDialog, QHeaderView
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QModelIndex

from scr.view.ui_students import Ui_students
from scr.models.datos import EstudiantesDAO, PoblacionesDAO
from scr.controller.estudiante_create_edit_controller import EstudianteController
from scr.util.message_box import MessageBox

class StudentsController(QDialog):
    """
    Controlador de la interfaz para gestionar estudiantes. Esta clase se encarga de manejar la interacción con la
    UI, los eventos, y la lógica asociada a la gestión de estudiantes.
    """
    
    def __init__(self):
        """
        Constructor de la clase, inicializa la interfaz de usuario y configura los eventos necesarios.
        """
        super().__init__()  # Llama al constructor de la clase base QDialog
        self.controlador = None
        self.model = None
        self.dao_estudiante = None
        self.estudiante_seleccionado = None
        self.ui = Ui_students()  # Instancia la UI de los estudiantes
        self.ui.setupUi(self)  # Configura la interfaz de usuario
        self.init_ui()  # Llama al método para inicializar la UI y los eventos

    def init_ui(self):
        """
        Método para configurar la interfaz de usuario y los eventos.
        """
        try:
            self.config_events()  # Configura los eventos de la UI
            self.config_table()  # Configura la tabla de estudiantes
            # self.load_poblaciones()  # Carga las poblaciones en el combobox
        except Exception as e:
            # En caso de error, se muestra un mensaje de error con la descripción
            MessageBox("Error al configurar la UI", "error", str(e)).show()

    def config_events(self):
        """
        Configura los eventos de la interfaz de usuario, como los clics en los botones.
        """
        # Conecta los botones a sus respectivas funciones
        self.ui.table_student.clicked.connect(self.click_estudiante)  # Evento de clic en la tabla de estudiantes
        self.ui.btn_modify.clicked.connect(lambda: self.open_modal(False))  # Evento de clic en "Modificar"
        self.ui.btn_new.clicked.connect(lambda: self.open_modal(True))  # Evento de clic en "Nuevo"

    def config_table(self):
        """
        Configura la tabla que muestra los estudiantes.
        """
        try:
            self.dao_estudiante = EstudiantesDAO()
            self.estudiante_seleccionado = None
            
            headers = ["Nombre", "Apellidos", "DNI", "Población", "Modalidad", "Usuario"]
            
            # Obtener la lista de estudiantes
            estudiantes = self.dao_estudiante.get_all()
            
            # Si get_all() devuelve un solo estudiante (no lista), lo convertimos a lista
            if estudiantes and not isinstance(estudiantes, list):
                estudiantes = [estudiantes]
            
            # Si no hay estudiantes, usamos lista vacía
            if not estudiantes:
                estudiantes = []
            
            # Crear modelo con el número de filas igual a la cantidad de estudiantes
            self.model = QStandardItemModel(len(estudiantes), len(headers))
            self.model.setHorizontalHeaderLabels(headers)

            # Rellenar la tabla con datos
            for row, estudiante in enumerate(estudiantes):
                poblacion_dao = PoblacionesDAO()
                poblacion = poblacion_dao.get(estudiante.id_poblacion)
                
                self.model.setItem(row, 0, QStandardItem(estudiante.nombre))
                self.model.setItem(row, 1, QStandardItem(estudiante.apellidos))
                self.model.setItem(row, 2, QStandardItem(estudiante.dni))
                self.model.setItem(row, 3, QStandardItem(poblacion.nombre if poblacion else ""))
                self.model.setItem(row, 4, QStandardItem(estudiante.modalidad))
                self.model.setItem(row, 5, QStandardItem(estudiante.usuario))
                # Guardamos el ID en la columna oculta
                self.model.setItem(row, 6, QStandardItem(str(estudiante.id_estudiante)))

            # Configurar la vista de tabla
            self.ui.table_student.setModel(self.model)
            self.ui.table_student.setColumnHidden(6, True)  # Ocultamos la columna ID
            self.ui.table_student.resizeColumnsToContents()
            self.ui.table_student.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.table_student.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.table_student.setSelectionMode(QAbstractItemView.SingleSelection)
            self.ui.table_student.setEditTriggers(QAbstractItemView.NoEditTriggers)
            
        except Exception as e:
            MessageBox("No se pudo cargar la tabla de estudiantes: {str(e)}", "error").show()

    def open_modal(self, nuevo: bool):
        """
        Abre un modal para la creación o modificación de un estudiante.
        
        :param nuevo: Si es True, abre el modal para crear un nuevo estudiante. 
                     Si es False, abre el modal para modificar el estudiante seleccionado.
        """
        if self.estudiante_seleccionado is not None or nuevo:
            if nuevo:
                self.controlador = EstudianteController(None)
            else:
                self.controlador = EstudianteController(self.estudiante_seleccionado)

            if not isinstance(self.controlador, QDialog):
                raise TypeError("El controlador debe heredar de QDialog para ser modal.")
            
            self.controlador.setModal(True)
            self.controlador.finished.connect(self.config_table)  # Actualiza tabla al cerrar
            self.controlador.exec()
        else:
            MessageBox("Seleccione un estudiante para ver los datos", "warning").show()

    def click_estudiante(self, index: QModelIndex):
        """
        Maneja el evento de clic en una fila de la tabla de estudiantes.
        
        :param index: Índice de la fila clickeada en la tabla.
        """
        row = index.row()
        estudiante_id_item = self.model.item(row, 6)  # Obtiene el valor de la columna "Id" (oculta)

        if estudiante_id_item:
            self.estudiante_seleccionado = int(estudiante_id_item.text()) if estudiante_id_item.text() else None

    def eliminar_estudiante(self):
        """
        Elimina el estudiante seleccionado de la base de datos.
        """
        if self.estudiante_seleccionado:
            confirmacion = MessageBox(
                "¿Está seguro de eliminar este estudiante?",
                "question",
                "Esta acción no se puede deshacer."
            ).show()
            
            if confirmacion:
                try:
                    self.dao_estudiante.delete(self.estudiante_seleccionado)
                    MessageBox("Estudiante eliminado correctamente", "info").show()
                    self.config_table()  # Actualiza la tabla
                    self.estudiante_seleccionado = None
                except Exception as e:
                    MessageBox("Error al eliminar estudiante", "error", str(e)).show()
        else:
            MessageBox("Seleccione un estudiante para eliminar", "warning").show()
