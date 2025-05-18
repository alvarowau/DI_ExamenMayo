from PySide6.QtWidgets import QWidget, QMessageBox, QDialog
from PySide6.QtCore import QDate
from scr.view.estudiantes_ui import Ui_Estudiantes
from scr.view.ui_register_students import Ui_students
from scr.util.message_box import MessageBox
from scr.util.validation import Validation
import re
from datetime import datetime
import re
from scr.models.repository import StudentRepository, CitiesRepository, ActivitiesRepository, StudentsActivitiesRepository
from scr.models.models import StudentEntity

class RegisterStudent(QDialog):
    """
    Controlador para la ventana de gestión de estudiantes, que permite la creación,
    modificación y visualización de estudiantes.
    """
    def __init__(self, student_id=None):
        """
        Constructor de la clase RegisterStudent.

        Parámetros:
        estudiante_id (int): ID del estudiante a editar. Si es None, se crea un nuevo estudiante.
        """
        self.student_activities_dao = None
        self.activities_dao = None
        self.cities_dao = None
        self.student_dao = None
        print(f"tiene id????? {student_id}")
        try:
            super().__init__()
            self.ui = Ui_students()
            self.ui.setupUi(self)

            self.initialize_daos()
            self.setup_events()
            self.is_minor = True

            if student_id:
                print(f"trae id y es: {student_id} y es tipo {type(student_id)}")
                self.student_id = student_id
                self.student = self.student_dao.get(self.student_id)
                self.is_new = False
                self.is_edit = False
            else:  # Nuevo estudiante
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
        """Inicializa los DAOs necesarios"""
        self.student_dao = StudentRepository()
        self.cities_dao = CitiesRepository()
        self.activities_dao = ActivitiesRepository()
        self.student_activities_dao = StudentsActivitiesRepository()

    def setup_events(self):
        """Configura los eventos de los botones"""
        self.ui.btn_save.clicked.connect(self.handle_save_button)
        self.ui.btn_delete.clicked.connect(self.close)
        self.ui.btn_delete.clicked.connect(self.handle_delete_button)
        self.ui.date_dob.dateChanged.connect(self.handle_date_change)

    def load_cities(self):
        """Carga las poblaciones en el combobox"""
        self.ui.combo_city.clear()
        cities = self.cities_dao.get_all()
        for city in cities:
            self.ui.combo_city.addItem(city.name, city.id_city)

    def load_activities(self):
        """Carga las actividades disponibles"""
        activities = self.activities_dao.get_all()
        # Asigna las actividades a los checkboxes correspondientes
        for activity in activities:
            if activity.name == "Danza":
                self.ui.check_danza.setText(activity.name)
            elif activity.name == "Ajedrez":
                self.ui.check_ajedrez.setText(activity.name)
            elif activity.name == "Fútbol":
                self.ui.check_futbol.setText(activity.name)

    def handle_date_change(self):
        """Maneja el cambio de fecha de nacimiento"""
        date = self.ui.date_dob.date().toPython()
        self.is_minor = self.check_if_minor(date)

        # Mostrar/ocultar campos de tutor según sea menor
        self.ui.txt_tlf.setVisible(self.is_minor)
        self.ui.line_tlf.setVisible(self.is_minor)
        self.ui.line_tutor.setVisible(self.is_minor)
        self.ui.txt_tutor.setVisible(self.is_minor)

    def check_if_minor(self, date_of_birth):
        """Determina si el estudiante es menor de age"""
        today = datetime.now()
        age = today.year - date_of_birth.year
        if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
            age -= 1
        return age < 18

    def change_mode(self):
        """Cambia entre modo edición y visualización"""
        if not self.is_edit:  # Modo visualización
            self.ui.btn_save.setText("Editar")
            self.ui.btn_delete.setText("Eliminar")
        else:  # Modo edición
            self.ui.btn_save.setText("Guardar")
            self.ui.btn_delete.setText("Cancelar")

        # Habilitar/deshabilitar campos según el modo
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
        """Inicializa la interfaz con los datos del estudiante"""
        self.setup_date()
        self.load_cities()
        self.ui.radio_distancia.setChecked(True)
        if not self.is_new:
            self.load_student_data()

    def setup_date(self):
        """Configura el widget de fecha"""
        current_date = QDate.currentDate()
        self.ui.date_dob.setDate(current_date)
        self.ui.date_dob.setMaximumDate(current_date)
        self.ui.date_dob.setCalendarPopup(True)
        self.ui.date_dob.setDisplayFormat("yyyy-MM-dd")

    def load_student_data(self):
        """Carga los datos del estudiante en la interfaz"""
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

            # Cargar actividades del estudiante
            student_activities = self.student_activities_dao.get_by_student(self.student.id_student)
            for activity in student_activities:
                if activity['actividad_nombre'] == "Danza":
                    self.ui.check_danza.setChecked(True)
                elif activity['actividad_nombre'] == "Ajedrez":
                    self.ui.check_ajedrez.setChecked(True)
                elif activity['actividad_nombre'] == "Fútbol":
                    self.ui.check_futbol.setChecked(True)

    def handle_save_button(self):
        """Maneja la acción del botón guardar/editar"""
        if self.is_edit:
            if self.validate_data():
                self.save_student()
                self.is_edit = False
                self.change_mode()
        else:
            self.is_edit = True
            self.change_mode()

    def handle_delete_button(self):
        """Maneja la acción del botón eliminar/cancelar"""
        if self.is_edit:
            self.is_edit = False
            self.change_mode()
            self.load_student_data()
        else:
            self.delete_student()

    def validate_data(self):
        """Valida los datos del formulario"""
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

    def generate_username(self, name, surnames):
        """Genera un name de user automático"""
        parts = surnames.strip().split()
        surname = parts[0]
        username = name[0].lower() + surname.lower()
        return username.replace(" ", "")

    def save_student(self):
        """Guarda o actualiza el estudiante en la base de datos"""
        name = self.ui.line_name.text().strip()
        surnames = self.ui.line_surname.text().strip()
        dni = self.ui.line_dni.text().strip()
        tutor = self.ui.line_tutor.text().strip() if self.is_minor else None
        phone = self.ui.line_tlf.text().strip() if self.is_minor else None
        distance = self.ui.spint_distant.value()
        city_id = self.ui.combo_city.currentData()
        modality = 'Presencial' if self.ui.radio_presencial.isChecked() else 'A Distancia'
        birth_date = self.ui.date_dob.date().toPython()
        username = self.generate_username(name, surnames)

        # Obtener actividades seleccionadas
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

            # Gestionar actividades
            self.student_activities_dao.remove_all_activities(self.student_id)
            activities = self.activities_dao.get_all()
            for activity in selected_activities:
                act_id = next(a.id_activity for a in activities if a.name == activity)
                self.student_activities_dao.add_activity(self.student_id, act_id)
            MessageBox("Estudiante guardado correctamente").show()

        except Exception as e:
            MessageBox(f"No se pudo guardar el estudiante: {str(e)}", "error").show()

    def delete_student(self):
        """Elimina el estudiante de la base de datos"""
        response = MessageBox("¿Desea eliminar este estudiante? Esto eliminará también toda la información relacionada", "question", buttons=("Yes", "No")).show()

        if response == "Yes":
            # Elimina las reservas y al cliente
            self.student_activities_dao.remove_all_activities(self.student_id)
            self.student_dao.delete(self.student_id)
            response = MessageBox("Estudiante eliminado").show() # Muestra mensaje de éxito
            if response:
                self.accept()  # Cierra la ventana de cliente
                self.close()

    def clear_form(self):
        """Limpia el formulario"""
        self.ui.line_name.clear()
        self.ui.line_surname.clear()
        self.ui.line_dni.clear()
        self.ui.line_tutor.clear()
        self.ui.line_tlf.clear()
        self.setup_date()
        self.ui.spint_distant.setValue(0)
        self.ui.combo_city.setCurrentIndex(0)
        self.ui.radio_presencial.setChecked(True)
        self.ui.radio_distancia.setChecked(False)
        self.ui.check_danza.setChecked(False)
        self.ui.check_ajedrez.setChecked(False)
        self.ui.check_futbol.setChecked(False)