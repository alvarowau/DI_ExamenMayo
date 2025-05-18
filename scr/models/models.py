from datetime import datetime

class StudentEntity:
    def __init__(self, id_student, name, surname, dni, date_birth, id_city,
                 distance, modality, user, tutor=None, phone_tutor=None, registration_date=None):
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
        return (f"Student(id={self.id_student}, name='{self.name}', surname='{self.surname}', "
                f"dni='{self.dni}', birth={self.date_birth.strftime('%Y-%m-%d') if self.date_birth else None}, "
                f"city_id={self.id_city}, distance={self.distance}, modality='{self.modalidad}', "
                f"user='{self.user}', tutor='{self.tutor}', phone='{self.phone_tutor}', "
                f"registration={self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_registro else None})")

    @property
    def is_minor(self):
        today = datetime.now()
        age = today.year - self.date_birth.year
        if (today.month, today.day) < (self.date_birth.month, self.date_birth.day):
            age -= 1
        return age < 18

class CityEntity:
    def __init__(self, id_city, name):
        self.id_city = id_city
        self.name = name

    def __str__(self):
        return f"City(id={self.id_city}, name='{self.name}')"

class ActivityEntity:
    def __init__(self, id_activity, name):
        self.id_activity = id_activity
        self.name = name

    def __str__(self):
        return f"Activity(id={self.id_activity}, name='{self.name}')"

class StudentActivityEntity:
    def __init__(self, id_student_activity, id_student, id_activity):
        self.id_student_activity = id_student_activity
        self.id_student = id_student
        self.id_activity = id_activity

    def __str__(self):
        return f"StudentActivity(id={self.id_student_activity}, student_id={self.id_student}, activity_id={self.id_activity})"

