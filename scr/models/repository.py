import mysql.connector
from scr.models.models import CityEntity, ActivityEntity, StudentEntity
from scr.models.config import DBConfig

class Repository:
    def __init__(self):
        config = DBConfig.get_config()

        db = config.get("db")
        user = config.get("user")
        psw = config.get("psw")
        port = config.get("port")
        host = config.get("host")

        if not all([db, user, psw, port, host]):
            raise ValueError("Faltan datos de conexión a la BD.")

        self.conn = mysql.connector.connect(
            user=user, password=psw, port=port, host=host, database=db
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def execute_query(self, query, params=None, fetch_one=False):
        self.cursor.execute(query, params or ())
        if query.strip().upper().startswith("SELECT"):
            return self.cursor.fetchone() if fetch_one else self.cursor.fetchall()
        else:
            self.conn.commit()
            return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()

class Queries:
    """Queries de poblaciones"""
    CITY_GET_BY_ID = "select * from poblaciones WHERE id_poblacion = %s"
    CITY_GET_ALL = "SELECT * FROM poblaciones"

    """Queries de actividades"""
    ACTIVITY_GET_BY_ID = "SELECT * FROM actividades WHERE id_actividad = %s"
    ACTIVITY_GET_ALL = "SELECT * FROM actividades"

    """Queries de estudiantes"""
    STUDENT_GET_BY_ID = "SELECT * FROM estudiantes WHERE id_estudiante = %s"
    STUDENT_GET_ALL = "SELECT * FROM estudiantes"
    STUDENT_INSERT = """
        INSERT INTO estudiantes 
        (nombre, apellidos, dni, fecha_nacimiento, id_poblacion, distancia_centro, 
         modalidad, usuario, tutor, telefono_tutor)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    STUDENT_UPDATE = """
        UPDATE estudiantes 
        SET nombre = %s, apellidos = %s, dni = %s, fecha_nacimiento = %s, 
            id_poblacion = %s, distancia_centro = %s, modalidad = %s, 
            usuario = %s, tutor = %s, telefono_tutor = %s
        WHERE id_estudiante = %s
        """
    STUDENT_DELETE = "DELETE FROM estudiantes WHERE id_estudiante = %s"
    STUDENT_EXIT_DNI = "SELECT * FROM estudiantes WHERE dni = %s"


    """queries student and activities"""
    STAC_BY_ID_ACTIVITIES = """
        SELECT ea.*, a.nombre as actividad_nombre 
        FROM estudiante_actividades ea
        JOIN actividades a ON ea.id_actividad = a.id_actividad
        WHERE ea.id_estudiante = %s
        """

    STAC_ADD_STUDENT_ACTIVITIES = """
        INSERT INTO estudiante_actividades (id_estudiante, id_actividad)
        VALUES (%s, %s)
        """
    STAC_REMOVE_STUDENT_ACTIVITIES = "DELETE FROM estudiante_actividades WHERE id_estudiante_actividad = %s"
    STAC_REMOVE_ALL_STUDENT_ACTIVITIES = "DELETE FROM estudiante_actividades WHERE id_estudiante = %s"

    """queries de usuarios"""
    USER_CREDENTIAL = "SELECT * FROM usuarios WHERE usuario = %s AND contrasenia = %s"

class CitiesRepository(Repository):
    def get(self, city_id):
        row = self.execute_query(Queries.CITY_GET_BY_ID, (city_id,), fetch_one=True)
        if row:
            return CityEntity(row['id_poblacion'], row['nombre'])
        return None

    def get_all(self):
        rows = self.execute_query(Queries.CITY_GET_ALL)
        return [CityEntity(row['id_poblacion'], row['nombre']) for row in rows]

class ActivitiesRepository(Repository):
    def get(self, activity_id):
        row = self.execute_query(Queries.ACTIVITY_GET_BY_ID, (activity_id,), fetch_one=True)
        if row:
            return ActivityEntity(row['id_actividad'], row['nombre'])
        return None

    def get_all(self):
        rows = self.execute_query(Queries.ACTIVITY_GET_ALL)
        return [ActivityEntity(row['id_actividad'], row['nombre']) for row in rows]

class StudentRepository(Repository):
    def get(self, student_id):
        row = self.execute_query(Queries.STUDENT_GET_BY_ID, (student_id,), fetch_one=True)
        if row:
            return StudentEntity(row['id_estudiante'], row['nombre'], row['apellidos'], row['dni'],
                row['fecha_nacimiento'], row['id_poblacion'], row['distancia_centro'],
                row['modalidad'], row['usuario'], row['tutor'], row['telefono_tutor'],
                row['fecha_registro'])
        return None

    def get_all(self):
        rows = self.execute_query(Queries.STUDENT_GET_ALL)
        return [
            StudentEntity(row['id_estudiante'], row['nombre'], row['apellidos'], row['dni'],
                row['fecha_nacimiento'], row['id_poblacion'], row['distancia_centro'],
                row['modalidad'], row['usuario'], row['tutor'], row['telefono_tutor'],
                row['fecha_registro']) for row in rows
        ]

    def create(self, student: StudentEntity):

        student_id = self.execute_query(Queries.STUDENT_INSERT, (
            student.name, student.surname, student.dni, student.date_birth,
            student.id_city, student.distance, student.modalidad,
            student.user, student.tutor, student.phone_tutor
        ))
        return self.get(student_id)

    def update(self, student: StudentEntity):

        self.execute_query(Queries.STUDENT_UPDATE, (
            student.name, student.surname, student.dni, student.date_birth,
            student.id_city, student.distance, student.modalidad,
            student.user, student.tutor, student.phone_tutor, student.id_student
        ))
        return self.get(student.id_student)

    def delete(self, student_id):
        self.execute_query(Queries.STUDENT_DELETE, (student_id,))

    def check_dni_exists(self, dni, student_id=None):
        params = (dni,)
        if student_id:
            Queries.STUDENT_EXIT_DNI += " AND id_student != %s"
            params = (dni, student_id)
        row = self.execute_query(Queries.STUDENT_EXIT_DNI, params, fetch_one=True)
        return row is not None

class StudentsActivitiesRepository(Repository):
    def get_by_student(self, student_id):
        rows = self.execute_query(Queries.STAC_BY_ID_ACTIVITIES, (student_id,))
        return [
            {
                'id_student_activity': row['id_estudiante_actividad'],
                'id_student': row['id_estudiante'],
                'id_activity': row['id_actividad'],
                'actividad_nombre': row['actividad_nombre']
            } for row in rows
        ]

    def add_activity(self, student_id, activity_id):
        self.execute_query(Queries.STAC_ADD_STUDENT_ACTIVITIES, (student_id, activity_id))

    def remove_activity(self, student_activity_id):
        self.execute_query(Queries.STAC_REMOVE_STUDENT_ACTIVITIES, (student_activity_id,))

    def remove_all_activities(self, student_id):
        self.execute_query(Queries.STAC_REMOVE_ALL_STUDENT_ACTIVITIES, (student_id,))

class UserDAO(Repository):
    def check_credentials(self, user, password):
        row = self.execute_query(Queries.USER_CREDENTIAL, (user, password), fetch_one=True)
        return row is not None  # Devuelve True si existe el user con la contraseña correcta, False si no
