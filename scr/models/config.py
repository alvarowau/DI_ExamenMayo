class DBConfig:
    """Clase para gestión centralizada de configuración de base de datos.

    Implementa el patrón Singleton a nivel de clase para almacenar y proporcionar
    la configuración de conexión a la base de datos para toda la aplicación.

    Atributos:
        _config (dict): Diccionario privado que almacena la configuración.
            Formato esperado:
            {
                "host": str,     # Dirección del servidor
                "port": int,     # Puerto de conexión
                "user": str,      # Usuario de la base de datos
                "psw": str,      # Contraseña
                "db": str        # Nombre de la base de datos
            }
    """

    _config = {}  # Diccionario privado para la configuración

    @classmethod
    def set_config(cls, config: dict):
        """Establece la configuración de conexión a la base de datos.

        Args:
            config (dict): Diccionario con los parámetros de conexión.
                Debe contener las claves: host, port, user, psw, db.

        Example:
            DBConfig.set_config({
                "host": "localhost",
                "port": 3306,
                "user": "admin",
                "psw": "password",
                "db": "mi_base_datos"
            })
        """
        cls._config = config

    @classmethod
    def get_config(cls) -> dict:
        """Obtiene la configuración actual de la base de datos.

        Returns:
            dict: Diccionario con la configuración actual. Devuelve un
                diccionario vacío si no se ha establecido configuración.
        """
        return cls._config