from PySide6.QtWidgets import QAbstractItemView, QDialog, QHeaderView
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QModelIndex

from scr.view.ui_students import Ui_students
from scr.models.repository import StudentRepository, CitiesRepository
from scr.controller.register_students_controller import RegisterStudent
from scr.util.message_box import MessageBox


class StudentsController(QDialog):
    """
    Controlador de la interfaz para gestionar estudiantes. Esta clase se encarga de manejar la interacción con la
    UI, los eventos, y la lógica asociada a la gestión de estudiantes.
    """

    def __init__(self):
        """
        Constructor de la clase, inicializa la interfaz de user y configura los eventos necesarios.
        """
        super().__init__()  # Llama al constructor de la clase base QDialog
        self.controller = None
        self.model = None
        self.student_dao = None
        self.selected_student = None
        self.ui = Ui_students()  # Instancia la UI de los estudiantes
        self.ui.setupUi(self)  # Configura la interfaz de user
        self.initialize_ui()  # Llama al método para inicializar la UI y los eventos

    def initialize_ui(self):
        """
        Método para configurar la interfaz de user y los eventos.
        """
        try:
            self.setup_events()  # Configura los eventos de la UI
            self.setup_table()  # Configura la tabla de estudiantes
            # self.load_poblaciones()  # Carga las poblaciones en el combobox
        except Exception as e:
            # En caso de error, se muestra un mensaje de error con la descripción
            MessageBox("Error al configurar la UI", "error", str(e)).show()

    def setup_events(self):
        """
        Configura los eventos de la interfaz de user, como los clics en los botones.
        """
        # Conecta los botones a sus respectivas funciones
        self.ui.table_student.clicked.connect(self.on_student_click)  # Evento de clic en la tabla de estudiantes
        self.ui.btn_modify.clicked.connect(lambda: self.open_modal(False))  # Evento de clic en "Modificar"
        self.ui.btn_new.clicked.connect(lambda: self.open_modal(True))  # Evento de clic en "Nuevo"

    def setup_table(self):
        """
        Configura la tabla que muestra los estudiantes.
        """
        try:
            self.student_dao = StudentRepository()
            self.selected_student = None

            headers = ["Nombre", "Apellidos", "DNI", "Población", "Modalidad", "Usuario"]

            # Obtener la lista de estudiantes
            students = self.student_dao.get_all()

            # Si get_all() devuelve un solo estudiante (no lista), lo convertimos a lista
            if students and not isinstance(students, list):
                students = [students]

            # Si no hay estudiantes, usamos lista vacía
            if not students:
                students = []

            # Crear modelo con el número de filas igual a la cantidad de estudiantes
            self.model = QStandardItemModel(len(students), len(headers))
            self.model.setHorizontalHeaderLabels(headers)

            # Rellenar la tabla con datos
            for row, student in enumerate(students):
                city_dao = CitiesRepository()
                city = city_dao.get(student.id_city)

                self.model.setItem(row, 0, QStandardItem(student.name))
                self.model.setItem(row, 1, QStandardItem(student.surname))
                self.model.setItem(row, 2, QStandardItem(student.dni))
                self.model.setItem(row, 3, QStandardItem(city.name if city else ""))
                self.model.setItem(row, 4, QStandardItem(student.modalidad))
                self.model.setItem(row, 5, QStandardItem(student.user))
                # Guardamos el ID en la columna oculta
                self.model.setItem(row, 6, QStandardItem(str(student.id_student)))

            # Configurar la vista de tabla
            self.ui.table_student.setModel(self.model)
            self.ui.table_student.setColumnHidden(6, True)  # Ocultamos la columna ID
            self.ui.table_student.resizeColumnsToContents()
            self.ui.table_student.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.table_student.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.table_student.setSelectionMode(QAbstractItemView.SingleSelection)
            self.ui.table_student.setEditTriggers(QAbstractItemView.NoEditTriggers)

        except Exception as e:
            print(str(e))
            MessageBox("No se pudo cargar la tabla de estudiantes", "error", details=str(e)).show()

    def open_modal(self, new: bool):
        """
        Abre un modal para la creación o modificación de un estudiante.

        :param nuevo: Si es True, abre el modal para crear un nuevo estudiante.
                     Si es False, abre el modal para modificar el estudiante seleccionado.
        """
        if self.selected_student is not None or new:
            if new:
                self.controller = RegisterStudent(None)
            else:
                self.controller = RegisterStudent(self.selected_student)

            if not isinstance(self.controller, QDialog):
                raise TypeError("El controlador debe heredar de QDialog para ser modal.")

            self.controller.setModal(True)
            self.controller.finished.connect(self.setup_table)  # Actualiza tabla al cerrar
            self.controller.exec()
        else:
            MessageBox("Seleccione un estudiante para ver los datos", "warning").show()

    def on_student_click(self, index: QModelIndex):
        """
        Maneja el evento de clic en una fila de la tabla de estudiantes.

        :param index: Índice de la fila clickeada en la tabla.
        """
        row = index.row()
        student_id_item = self.model.item(row, 6)  # Obtiene el valor de la columna "Id" (oculta)

        if student_id_item:
            self.selected_student = int(student_id_item.text()) if student_id_item.text() else None

    def delete_student(self):
        """
        Elimina el estudiante seleccionado de la base de datos.
        """
        if self.selected_student:
            Confirmation = MessageBox(
                "¿Está seguro de eliminar este estudiante?",
                "question",
                "Esta acción no se puede deshacer."
            ).show()

            if Confirmation:
                try:
                    self.student_dao.delete(self.selected_student)
                    MessageBox("Estudiante eliminado correctamente", "info").show()
                    self.setup_table()  # Actualiza la tabla
                    self.selected_student = None
                except Exception as e:
                    MessageBox("Error al eliminar estudiante", "error", str(e)).show()
        else:
            MessageBox("Seleccione un estudiante para eliminar", "warning").show()
