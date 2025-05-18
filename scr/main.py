#!/usr/bin/python3
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from scr.controller.login_controller import LoginController
from scr.controller.connection_controller import ConnectionController
from scr.controller.students_controller import StudentsController


def login(app):
    """Maneja la ventana de login y retorna el estado de autenticación.

    Gestiona la visualización de la ventana de login y el proceso de autenticación.
    La función se bloquea hasta que se cierra la ventana de login.

    Args:
        app (QApplication): Instancia de la aplicación Qt para ejecutar el bucle de eventos.

    Returns:
        bool: True si el login fue exitoso (bLogado es True), False en caso contrario.
    """
    login_window = QMainWindow()
    login_controller = LoginController(login_window)
    login_window.show()
    app.exec()
    return login_controller.bLogado


def init_app(app):
    """Inicializa la aplicación principal después de un login exitoso.

    Crea la conexión a la base de datos y muestra la ventana principal de la aplicación.

    Args:
        app (QApplication): Instancia de la aplicación Qt para ejecutar el bucle de eventos.
    """
    main_window = StudentsController()
    main_window.setModal(True)
    main_window.show()
    app.exec()


def main():
    """Función principal que coordina el flujo de la aplicación.

    Gestiona el proceso completo:
    1. Muestra la ventana de configuración de conexión
    2. Si la conexión es aceptada, muestra el login
    3. Si el login es exitoso, inicia la aplicación principal
    """
    app = QApplication(sys.argv)

    config_window = ConnectionController()
    config_window.setModal(True)

    if config_window.exec() == QDialog.Accepted:
        if login(app):
            init_app(app)


if __name__ == "__main__":
    main()