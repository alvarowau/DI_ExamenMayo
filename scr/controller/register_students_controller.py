from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from scr.view.ui_register_students import Ui_students
from scr.util.message_box import MessageBox
from scr.util.validation import Validation
from datetime import datetime
from scr.models.repository import StudentRepository, CitiesRepository, ActivitiesRepository, StudentsActivitiesRepository
from scr.models.models import StudentEntity


def generate_username(name, surnames):
    """Genera un nombre de usuario automático.
    Args:
        name (str): Nombre del estudiante
        surnames (str): Apellidos del estudiante

    Returns:
        str: Nombre de usuario generado
    """
    parts = surnames.strip().split()
    surname = parts[0]
    username = name[0].lower() + surname.lower()
    return username.replace(" ", "")


def check_if_minor(date_of_birth):
    """Determina si el estudiante es menor de edad.

    Args:
        date_of_birth (datetime.date): Fecha de nacimiento del estudiante

    Returns:
        bool: True si es menor de edad, False en caso contrario
    """
    today = datetime.now()
    age = today.year - date_of_birth.year
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1
    return age < 18


class RegisterStudent(QDialog):
    """Controlador para la ventana de gestión de estudiantes.

    Permite la creación, modificación y visualización de estudiantes, incluyendo:
    - Gestión de datos personales
    - Asignación de actividades
    - Validación de campos
    - Manejo de modos de edición/visualización

    Atributos:
        student_activities_dao (StudentsActivitiesRepository): DAO para actividades de estudiantes
        activities_dao (ActivitiesRepository): DAO para actividades
        cities_dao (CitiesRepository): DAO para ciudades
        student_dao (StudentRepository): DAO para estudiantes
        student_id (int): ID del estudiante actual
        student (StudentEntity): Datos del estudiante actual
        is_new (bool): Indica si es un nuevo estudiante
        is_edit (bool): Indica si está en modo edición
        is_minor (bool): Indica si el estudiante es menor de edad
        ui (Ui_students): Interfaz gráfica del formulario
    """

    def __init__(self, student_id=None):
        """Inicializa el controlador del formulario de estudiantes.

        Args:
            student_id (int, optional): ID del estudiante a editar. None para nuevo estudiante.
        """
        self.student_activities_dao = None
        self.activities_dao = None
        self.cities_dao = None
        self.student_dao = None
        try:
            super().__init__()
            self.ui = Ui_students()
            self.ui.setupUi(self)

            self.initialize_daos()
            self.setup_events()
            self.is_minor = True

            if student_id:
                self.student_id = student_id
                if self.student_dao:
                    self.student = self.student_dao.get(self.student_id)
                self.is_new = False
                self.is_edit = False
            else:
                self.student_id = None
                self.student = None
                self.is_new = True
                self.is_edit = True
                self.ui.btn_delete.setVisible(False)

            self.change_mode()
            self.initialize_ui()

        except Exception as e:
            MessageBox(f"Error al cargar el formulario: {str(e)}", "error").show()

    def initialize_daos(self):
        """Inicializa los objetos de acceso a datos necesarios."""
        self.student_dao = StudentRepository()
        self.cities_dao = CitiesRepository()
        self.activities_dao = ActivitiesRepository()
        self.student_activities_dao = StudentsActivitiesRepository()

    def setup_events(self):
        """Configura los eventos de los controles de la interfaz."""
        self.ui.btn_save.clicked.connect(self.handle_save_button)
        self.ui.btn_delete.clicked.connect(self.close)
        self.ui.btn_delete.clicked.connect(self.handle_delete_button)
        self.ui.date_dob.dateChanged.connect(self.handle_date_change)

    def load_cities(self):
        """Carga las ciudades disponibles en el combobox correspondiente."""
        self.ui.combo_city.clear()
        cities = self.cities_dao.get_all()
        for city in cities:
            self.ui.combo_city.addItem(city.name, city.id_city)

    def load_activities(self):
        """Carga las actividades disponibles y las asigna a los checkboxes."""
        activities = self.activities_dao.get_all()
        for activity in activities:
            if activity.name == "Danza":
                self.ui.check_danza.setText(activity.name)
            elif activity.name == "Ajedrez":
                self.ui.check_ajedrez.setText(activity.name)
            elif activity.name == "Fútbol":
                self.ui.check_futbol.setText(activity.name)

    def handle_date_change(self):
        """Maneja el cambio en la fecha de nacimiento del estudiante."""
        date = self.ui.date_dob.date().toPython()
        self.is_minor = check_if_minor(date)

        self.ui.txt_tlf.setVisible(self.is_minor)
        self.ui.line_tlf.setVisible(self.is_minor)
        self.ui.line_tutor.setVisible(self.is_minor)
        self.ui.txt_tutor.setVisible(self.is_minor)

    def change_mode(self):
        """Alterna entre modo edición y modo visualización."""
        if not self.is_edit:
            self.ui.btn_save.setText("Editar")
            self.ui.btn_delete.setText("Eliminar")
        else:
            self.ui.btn_save.setText("Guardar")
            self.ui.btn_delete.setText("Cancelar")

        self.ui.line_name.setEnabled(self.is_edit)
        self.ui.line_surname.setEnabled(self.is_edit)
        self.ui.line_dni.setEnabled(self.is_edit)
        self.ui.date_dob.setEnabled(self.is_edit)
        self.ui.combo_city.setEnabled(self.is_edit)
        self.ui.spint_distant.setEnabled(self.is_edit)
        self.ui.radio_presencial.setEnabled(self.is_edit)
        self.ui.radio_distancia.setEnabled(self.is_edit)
        self.ui.check_danza.setEnabled(self.is_edit)
        self.ui.check_ajedrez.setEnabled(self.is_edit)
        self.ui.check_futbol.setEnabled(self.is_edit)
        self.ui.line_tutor.setEnabled(self.is_edit)
        self.ui.line_tlf.setEnabled(self.is_edit)

    def initialize_ui(self):
        """Inicializa la interfaz con los datos del estudiante."""
        self.setup_date()
        self.load_cities()
        self.ui.radio_distancia.setChecked(True)
        if not self.is_new:
            self.load_student_data()

    def setup_date(self):
        """Configura el widget de fecha con valores iniciales."""
        current_date = QDate.currentDate()
        self.ui.date_dob.setDate(current_date)
        self.ui.date_dob.setMaximumDate(current_date)
        self.ui.date_dob.setCalendarPopup(True)
        self.ui.date_dob.setDisplayFormat("yyyy-MM-dd")

    def load_student_data(self):
        """Carga los datos del estudiante en los controles del formulario."""
        if self.student:
            self.ui.line_name.setText(self.student.name)
            self.ui.line_surname.setText(self.student.surname)
            self.ui.line_dni.setText(self.student.dni)

            birth_date = QDate.fromString(str(self.student.date_birth), "yyyy-MM-dd")
            self.ui.date_dob.setDate(birth_date)

            self.ui.combo_city.setCurrentText(self.cities_dao.get(self.student.id_city).name)
            self.ui.spint_distant.setValue(float(self.student.distance))

            if self.student.modalidad == 'Presencial':
                self.ui.radio_presencial.setChecked(True)
            else:
                self.ui.radio_distancia.setChecked(True)

            if self.student.tutor:
                self.ui.line_tutor.setText(self.student.tutor)
                self.ui.line_tlf.setText(self.student.phone_tutor)

            student_activities = self.student_activities_dao.get_by_student(self.student.id_student)
            for activity in student_activities:
                if activity['actividad_nombre'] == "Danza":
                    self.ui.check_danza.setChecked(True)
                elif activity['actividad_nombre'] == "Ajedrez":
                    self.ui.check_ajedrez.setChecked(True)
                elif activity['actividad_nombre'] == "Fútbol":
                    self.ui.check_futbol.setChecked(True)

    def handle_save_button(self):
        """Maneja el evento de clic en el botón Guardar/Editar."""
        if self.is_edit:
            if self.validate_data():
                self.save_student()
                self.is_edit = False
                self.change_mode()
        else:
            self.is_edit = True
            self.change_mode()

    def handle_delete_button(self):
        """Maneja el evento de clic en el botón Eliminar/Cancelar."""
        if self.is_edit:
            self.is_edit = False
            self.change_mode()
            self.load_student_data()
        else:
            self.delete_student()

    def validate_data(self):
        """Valida los datos ingresados en el formulario.

        Returns:
            bool: True si los datos son válidos, False en caso contrario
        """
        name = not Validation.is_empty(self.ui.line_name.text().strip())
        surname = not Validation.is_empty(self.ui.line_surname.text().strip())
        dni = not Validation.is_empty(self.ui.line_dni.text().strip())
        tutor = self.ui.line_tutor.text().strip()
        phone = self.ui.line_tlf.text().strip()

        if not (name and surname and dni):
            MessageBox("Por favor, complete todos los campos requeridos.", "warning").show()
            return False

        if self.is_minor and not (tutor and phone):
            MessageBox("Por favor, complete todos los datos del tutor.", "warning").show()
            return False

        if not dni and Validation.is_valid_dni(self.ui.line_dni.text().strip()):
            MessageBox("NIF no válido", "warning").show()
            return False

        return True

    def save_student(self):
        """Guarda o actualiza los datos del estudiante en la base de datos."""
        name = self.ui.line_name.text().strip()
        surnames = self.ui.line_surname.text().strip()
        dni = self.ui.line_dni.text().strip()
        tutor = self.ui.line_tutor.text().strip() if self.is_minor else None
        phone = self.ui.line_tlf.text().strip() if self.is_minor else None
        distance = self.ui.spint_distant.value()
        city_id = self.ui.combo_city.currentData()
        modality = 'Presencial' if self.ui.radio_presencial.isChecked() else 'A Distancia'
        birth_date = self.ui.date_dob.date().toPython()
        username = generate_username(name, surnames)

        selected_activities = []
        if self.ui.check_danza.isChecked():
            selected_activities.append("Danza")
        if self.ui.check_ajedrez.isChecked():
            selected_activities.append("Ajedrez")
        if self.ui.check_futbol.isChecked():
            selected_activities.append("Fútbol")

        student = StudentEntity(id_student=self.student_id if not self.is_new else None, name=name,
                               surname=surnames, dni=dni, date_birth=birth_date, id_city=city_id,
                               distance=distance, modality=modality, user=username, tutor=tutor,
                               phone_tutor=phone)

        try:
            if self.is_new:
                new_id = self.student_dao.create(student).id_student
                self.student_id = new_id
                self.is_new = False
                self.ui.btn_delete.setVisible(True)
            else:
                self.student_dao.update(student)

            self.student_activities_dao.remove_all_activities(self.student_id)
            activities = self.activities_dao.get_all()
            for activity in selected_activities:
                act_id = next(a.id_activity for a in activities if a.name == activity)
                self.student_activities_dao.add_activity(self.student_id, act_id)
            MessageBox("Estudiante guardado correctamente").show()

        except Exception as e:
            MessageBox(f"No se pudo guardar el estudiante: {str(e)}", "error").show()

    def delete_student(self):
        """Elimina el estudiante de la base de datos después de confirmación."""
        response = MessageBox("¿Desea eliminar este estudiante? Esto eliminará también toda la información relacionada", "question", buttons=("Yes", "No")).show()

        if response == "Yes":
            self.student_activities_dao.remove_all_activities(self.student_id)
            self.student_dao.delete(self.student_id)
            response = MessageBox("Estudiante eliminado").show()
            if response:
                self.accept()
                self.close()
