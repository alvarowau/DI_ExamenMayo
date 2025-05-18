from PySide6.QtWidgets import QDialog
from scr.models.config import DBConfig
from scr.models.repository import Repository
from scr.util.message_box import MessageBox
from scr.view.ui_connection_db import Ui_connection_bd


class ConnectionController(QDialog):
    """Controlador para la configuración de conexión a base de datos.

    Permite al usuario especificar los parámetros de conexión a la base de datos
    y verifica que la conexión sea válida antes de aceptar la configuración.

    Atributos:
        ui (Ui_connection_bd): Interfaz gráfica del diálogo de conexión.
    """

    def __init__(self):
        """Inicializa el diálogo de configuración con valores por defecto.

        Configura los campos de la interfaz con valores predeterminados y
        conecta las señales de los botones a sus respectivos manejadores.
        """
        super().__init__()
        self.ui = Ui_connection_bd()
        self.ui.setupUi(self)
        self.ui.line_host.setText('localhost')
        self.ui.line_port.setText('3307')
        self.ui.line_user.setText('root')
        self.ui.line_password.setText('root')
        self.ui.line_bd.setText('EXAMEN2DI')

        self.ui.btn_acept.clicked.connect(self.save_config)

    def save_config(self):
        """Guarda la configuración y prueba la conexión con la base de datos.

        Recoge los valores de los campos de texto, los almacena en la configuración
        y verifica que la conexión sea posible. Muestra un mensaje con el resultado.

        Raises:
            Exception: Si ocurre algún error durante la conexión a la base de datos.
        """
        config = {
            "host": self.ui.line_host.text(),
            "port": int(self.ui.line_port.text()) if self.ui.line_port.text().isdigit() else 3306,
            "user": self.ui.line_user.text(),
            "psw": self.ui.line_password.text(),
            "db": self.ui.line_bd.text(),
        }

        DBConfig.set_config(config)
        try:
            dao = Repository()
            dao.close()
            MessageBox("Conexión exitosa").show()
            self.accept()
        except Exception as e:
            MessageBox(f"Fallo en la conexión:\n{e}", "error").show()