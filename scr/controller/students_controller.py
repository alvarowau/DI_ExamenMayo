from PySide6.QtWidgets import QAbstractItemView, QDialog, QHeaderView
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QModelIndex

from scr.view.ui_students import Ui_students
from scr.models.repository import StudentRepository, CitiesRepository
from scr.controller.register_students_controller import RegisterStudent
from scr.util.message_box import MessageBox


class StudentsController(QDialog):
    """Controlador principal para la gestión de estudiantes.

    Esta clase maneja la interfaz principal de estudiantes, incluyendo:
    - Visualización de lista de estudiantes
    - Apertura de modales para edición/creación
    - Eliminación de estudiantes
    - Configuración de la tabla de visualización

    Atributos:
        controller (RegisterStudent): Controlador del modal de edición
        model (QStandardItemModel): Modelo de datos para la tabla
        student_dao (StudentRepository): Acceso a datos de estudiantes
        selected_student (int): ID del estudiante seleccionado
        ui (Ui_students): Interfaz gráfica de usuario
    """

    def __init__(self):
        """Inicializa el controlador y configura la interfaz."""
        super().__init__()
        self.controller = None
        self.model = None
        self.student_dao = None
        self.selected_student = None
        self.ui = Ui_students()
        self.ui.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        """Configura los componentes iniciales de la interfaz."""
        try:
            self.setup_events()
            self.setup_table()
        except Exception as e:
            MessageBox("Error al configurar la UI", "error", str(e)).show()

    def setup_events(self):
        """Configura los eventos de los controles de la interfaz."""
        self.ui.table_student.clicked.connect(self.on_student_click)
        self.ui.btn_modify.clicked.connect(lambda: self.open_modal(False))
        self.ui.btn_new.clicked.connect(lambda: self.open_modal(True))

    def setup_table(self):
        """Configura y carga los datos en la tabla de estudiantes."""
        try:
            self.student_dao = StudentRepository()
            self.selected_student = None

            headers = ["Nombre", "Apellidos", "DNI", "Población", "Modalidad", "Usuario"]
            students = self.student_dao.get_all()

            if students and not isinstance(students, list):
                students = [students]

            if not students:
                students = []

            self.model = QStandardItemModel(len(students), len(headers))
            self.model.setHorizontalHeaderLabels(headers)

            for row, student in enumerate(students):
                city_dao = CitiesRepository()
                city = city_dao.get(student.id_city)

                self.model.setItem(row, 0, QStandardItem(student.name))
                self.model.setItem(row, 1, QStandardItem(student.surname))
                self.model.setItem(row, 2, QStandardItem(student.dni))
                self.model.setItem(row, 3, QStandardItem(city.name if city else ""))
                self.model.setItem(row, 4, QStandardItem(student.modalidad))
                self.model.setItem(row, 5, QStandardItem(student.user))
                self.model.setItem(row, 6, QStandardItem(str(student.id_student)))

            self.ui.table_student.setModel(self.model)
            self.ui.table_student.setColumnHidden(6, True)
            self.ui.table_student.resizeColumnsToContents()
            self.ui.table_student.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.table_student.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.table_student.setSelectionMode(QAbstractItemView.SingleSelection)
            self.ui.table_student.setEditTriggers(QAbstractItemView.NoEditTriggers)

        except Exception as e:
            MessageBox("No se pudo cargar la tabla de estudiantes", "error", details=str(e)).show()

    def open_modal(self, new: bool):
        """Abre el diálogo para crear o editar un estudiante.

        Args:
            new (bool): Si es True, crea un nuevo estudiante. Si es False, edita el seleccionado.

        Raises:
            TypeError: Si el controlador no es un QDialog válido.
        """
        if self.selected_student is not None or new:
            if new:
                self.controller = RegisterStudent(None)
            else:
                self.controller = RegisterStudent(self.selected_student)

            if not isinstance(self.controller, QDialog):
                raise TypeError("El controlador debe heredar de QDialog para ser modal.")

            self.controller.setModal(True)
            self.controller.finished.connect(self.setup_table)
            self.controller.exec()
        else:
            MessageBox("Seleccione un estudiante para ver los datos", "warning").show()

    def on_student_click(self, index: QModelIndex):
        """Maneja la selección de un estudiante en la tabla.

        Args:
            index (QModelIndex): Índice de la fila seleccionada.
        """
        row = index.row()
        student_id_item = self.model.item(row, 6)

        if student_id_item:
            self.selected_student = int(student_id_item.text()) if student_id_item.text() else None

    def delete_student(self):
        """Elimina el estudiante seleccionado previa confirmación."""
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
                    self.setup_table()
                    self.selected_student = None
                except Exception as e:
                    MessageBox("Error al eliminar estudiante", "error", str(e)).show()
        else:
            MessageBox("Seleccione un estudiante para eliminar", "warning").show()
