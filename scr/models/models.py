from datetime import datetime


class StudentEntity:
    """Entidad que representa a un estudiante en el sistema.

    Atributos:
        id_student (int): Identificador único del estudiante
        name (str): Nombre del estudiante
        surname (str): Apellidos del estudiante
        dni (str): Documento Nacional de Identidad
        date_birth (datetime.date): Fecha de nacimiento
        id_city (int): ID de la ciudad de residencia
        distance (float): Distancia al centro educativo en km
        modalidad (str): Modalidad de estudio ('Presencial'/'A Distancia')
        user (str): Nombre de usuario en el sistema
        tutor (str, optional): Nombre del tutor (para menores de edad)
        phone_tutor (str, optional): Teléfono del tutor
        fecha_registro (datetime.datetime, optional): Fecha de registro en el sistema
    """

    def __init__(self, id_student, name, surname, dni, date_birth, id_city,
                 distance, modality, user, tutor=None, phone_tutor=None, registration_date=None):
        """Inicializa una nueva instancia de StudentEntity."""
        self.id_student = id_student
        self.name = name
        self.surname = surname
        self.dni = dni
        self.date_birth = date_birth
        self.id_city = id_city
        self.distance = distance
        self.modalidad = modality
        self.user = user
        self.tutor = tutor
        self.phone_tutor = phone_tutor
        self.fecha_registro = registration_date

    def __str__(self):
        """Representación en string del objeto StudentEntity.

        Returns:
            str: Cadena con los principales atributos del estudiante
        """
        return (f"Student(id={self.id_student}, name='{self.name}', surname='{self.surname}', "
                f"dni='{self.dni}', birth={self.date_birth.strftime('%Y-%m-%d') if self.date_birth else None}, "
                f"city_id={self.id_city}, distance={self.distance}, modality='{self.modalidad}', "
                f"user='{self.user}', tutor='{self.tutor}', phone='{self.phone_tutor}', "
                f"registration={self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_registro else None})")

    @property
    def is_minor(self):
        """Determina si el estudiante es menor de edad.

        Returns:
            bool: True si el estudiante es menor de 18 años, False en caso contrario
        """
        today = datetime.now()
        age = today.year - self.date_birth.year
        if (today.month, today.day) < (self.date_birth.month, self.date_birth.day):
            age -= 1
        return age < 18


class CityEntity:
    """Entidad que representa una ciudad/población en el sistema.

    Atributos:
        id_city (int): Identificador único de la ciudad
        name (str): Nombre de la ciudad
    """

    def __init__(self, id_city, name):
        """Inicializa una nueva instancia de CityEntity."""
        self.id_city = id_city
        self.name = name

    def __str__(self):
        """Representación en string del objeto CityEntity.

        Returns:
            str: Cadena con los atributos de la ciudad
        """
        return f"City(id={self.id_city}, name='{self.name}')"


class ActivityEntity:
    """Entidad que representa una actividad extraescolar.

    Atributos:
        id_activity (int): Identificador único de la actividad
        name (str): Nombre de la actividad (ej. 'Danza', 'Fútbol')
    """

    def __init__(self, id_activity, name):
        """Inicializa una nueva instancia de ActivityEntity."""
        self.id_activity = id_activity
        self.name = name

    def __str__(self):
        """Representación en string del objeto ActivityEntity.

        Returns:
            str: Cadena con los atributos de la actividad
        """
        return f"Activity(id={self.id_activity}, name='{self.name}')"


class StudentActivityEntity:
    """Entidad que relaciona estudiantes con actividades (N-M).

    Atributos:
        id_student_activity (int): Identificador único de la relación
        id_student (int): ID del estudiante relacionado
        id_activity (int): ID de la actividad relacionada
    """

    def __init__(self, id_student_activity, id_student, id_activity):
        """Inicializa una nueva instancia de StudentActivityEntity."""
        self.id_student_activity = id_student_activity
        self.id_student = id_student
        self.id_activity = id_activity

    def __str__(self):
        """Representación en string del objeto StudentActivityEntity.

        Returns:
            str: Cadena con los IDs de la relación
        """
        return f"StudentActivity(id={self.id_student_activity}, student_id={self.id_student}, activity_id={self.id_activity})"