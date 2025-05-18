#!/usr/bin/python3
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from scr.controller.login_controller import LoginController
from scr.controller.connection_controller import ConnectionController
from scr.controller.estudiantes_controller import EstudiantesController

def login(app):
    """
    Función que maneja la ventana de login y retorna si el usuario ha iniciado sesión correctamente.

    Args:
        app (QApplication): Instancia de la aplicación Qt que se utilizará para ejecutar el ciclo de eventos de la GUI.

    Returns:
        bool: Retorna True si el login fue exitoso, False en caso contrario.
    """
    login_window = QMainWindow()
    login_controller = LoginController(login_window)
    login_window.show()

    # Inicia el ciclo de evsentos de la aplicación Qt (esto hace que la ventana se muestre y se quede activa).
    app.exec()

    return login_controller.bLogado


def init_app(app):
    """
    Inicializa la aplicación principal después de un login exitoso.

    Esta función se encarga de crear la conexión a la base de datos y mostrar la ventana principal de la aplicación.

    Args:
        app (QApplication): Instancia de la aplicación Qt que se utilizará para ejecutar el ciclo de eventos de la GUI.
    """

    main_window = EstudiantesController()
    main_window.setModal(True)
    main_window.show()

    # Inicia el ciclo de eventos de la aplicación Qt, lo que permite que la ventana se mantenga abierta.
    app.exec()


def main():
    """
    Función principal que coordina el flujo de la aplicación.
    Inicia el proceso de login y, si es exitoso, inicializa la aplicación principal.
    """
    app = QApplication(sys.argv)

    config_window = ConnectionController()
    config_window.setModal(True)

    if config_window.exec() == QDialog.Accepted:
        if login(app):
            init_app(app)


# Bloque que asegura que el código se ejecute solo si el script es ejecutado directamente.
if __name__ == "__main__":
    main()
