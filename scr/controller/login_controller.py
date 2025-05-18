from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from scr.view.ui_login import Ui_Login
from scr.util.message_box import MessageBox
from scr.models.repository import UserDAO


class LoginController(Ui_Login, QObject):
    """Controlador para la ventana de autenticación de usuarios.

    Gestiona todo el proceso de inicio de sesión, incluyendo:
    - Validación de campos
    - Autenticación de credenciales
    - Retroalimentación al usuario
    - Cierre de sesión controlado

    Atributos:
        bLogado (bool): Bandera que indica si el login fue exitoso.
        ui (Ui_Login): Instancia de la interfaz gráfica de login.
        login_window (QWidget): Referencia a la ventana de login.
        usuarios_dao (UserDAO): Objeto para acceder a datos de usuarios.
    """

    def __init__(self, login_window: QWidget):
        """Inicializa el controlador de login con sus componentes.

        Args:
            login_window (QWidget): Ventana principal donde se mostrará el login.
        """
        self.bLogado = False
        super().__init__()
        self.ui = Ui_Login()
        self.login_window = login_window
        self.ui.setupUi(self.login_window)

        self.ui.line_user.setText('alvaro')
        self.ui.line_password.setText('alvaro')

        self.ui.btn_login.clicked.connect(self.login)

        self.usuarios_dao = UserDAO()

    def login(self):
        """Maneja el evento de click en el botón de login.

        Realiza las siguientes acciones:
        1. Obtiene y sanitiza los datos del formulario
        2. Valida campos obligatorios
        3. Autentica al usuario
        4. Proporciona feedback visual
        5. Cierra la ventana si la autenticación es exitosa
        """
        user = self.ui.line_user.text().strip()
        pwd = self.ui.line_password.text().strip()

        message = "Logado con éxito"
        msg_type = "error"

        self.bLogado = self.autenticar(user, pwd)

        if not user or not pwd:
            message = "Ambos campos son obligatorios"
        elif not self.bLogado:
            message = "Usuario o contraseña incorrectos"
        elif self.bLogado:
            msg_type = "success"

        MessageBox(message, msg_type).show()

        if self.bLogado:
            self.login_window.close()

    def autenticar(self, user: str, pwd: str) -> bool:
        """Autentica las credenciales del usuario contra la base de datos.

        Args:
            user (str): Nombre de usuario proporcionado.
            pwd (str): Contraseña proporcionada.

        Returns:
            bool: True si las credenciales son válidas, False en caso contrario.

        Notas:
            Utiliza el UserDAO para verificar las credenciales en la capa de persistencia.
            La contraseña debería manejarse de forma segura (hashing) en producción.
        """
        return self.usuarios_dao.check_credentials(user, pwd)