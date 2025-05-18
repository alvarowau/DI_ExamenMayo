from PySide6.QtWidgets import QDialog
from scr.models.config import DBConfig
from scr.models.repository import Repository
from scr.util.message_box import MessageBox
from scr.view.ui_connection_db import Ui_connection_bd

class ConnectionController(QDialog):
    '''
    Clase que se encarga de mostrar el apartado de "Conexion BD" para que el user indica a donde apunta la BD con la que va a trabajar
    '''
    def __init__(self):
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
        """Guarda la configuración y prueba la conexión a la BD."""
        config = {
            "host": self.ui.line_host.text(),
            "port": int(self.ui.line_port.text()) if self.ui.line_port.text().isdigit() else 3306,
            "user": self.ui.line_user.text(),
            "psw": self.ui.line_password.text(),
            "db": self.ui.line_bd.text(),
        }

        DBConfig.set_config(config)  # Guarda la configuración en DBConfig

        # Verificar conexión a la base de datos
        try:
            dao = Repository()  # Intenta conectar con la BD
            dao.close()  # Si funciona, cierra la conexión
            MessageBox("Conexión exitosa").show()
            self.accept()  # Cierra el diálogo con éxito
        except Exception as e:
            MessageBox(f"Fallo en la conexión:\n{e}", "error").show()
