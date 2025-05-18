from PySide6.QtWidgets import QMessageBox


class MessageBox(QMessageBox):
    """Clase personalizada para mostrar mensajes al usuario.

    Proporciona una interfaz unificada para mostrar diferentes tipos de mensajes
    (información, error, advertencia, éxito y preguntas) con soporte para:
    - Texto detallado
    - Botones personalizados
    - Iconos según tipo de mensaje

    Atributos heredados:
        Todos los atributos de QMessageBox
    """

    def __init__(self, message, message_type="info", details=None, buttons=("Ok",)):
        """Inicializa el cuadro de mensaje con configuración básica.

        Args:
            message (str): Mensaje principal a mostrar.
            message_type (str): Tipo de mensaje. Valores aceptados:
                'info', 'error', 'warning', 'success', 'question'.
                Default: 'info'
            details (str, optional): Texto adicional para sección detallada.
            buttons (tuple, optional): Tupla con nombres de botones a mostrar.
                Valores aceptados: 'Ok', 'Cancel', 'Yes', 'No', 'Retry', 'Ignore', 'Close'.
                Default: ('Ok',)
        """
        super().__init__()
        self.setWindowTitle(message_type.capitalize())
        self.setText(message)

        icon_mapping = {
            "info": QMessageBox.Icon.Information,
            "error": QMessageBox.Icon.Critical,
            "warning": QMessageBox.Icon.Warning,
            "success": QMessageBox.Icon.Information,
            "question": QMessageBox.Icon.Question,
        }
        self.setIcon(icon_mapping.get(message_type, QMessageBox.Icon.Information))

        if details:
            self.setDetailedText(details)

        button_mapping = {
            "Ok": QMessageBox.StandardButton.Ok,
            "Cancel": QMessageBox.StandardButton.Cancel,
            "Yes": QMessageBox.StandardButton.Yes,
            "No": QMessageBox.StandardButton.No,
            "Retry": QMessageBox.StandardButton.Retry,
            "Ignore": QMessageBox.StandardButton.Ignore,
            "Close": QMessageBox.StandardButton.Close,
        }

        selected_buttons = QMessageBox.StandardButton.NoButton
        for b in buttons:
            if b in button_mapping:
                selected_buttons |= button_mapping[b]

        self.setStandardButtons(selected_buttons)

    def show(self) -> str:
        """Muestra el diálogo de mensaje y espera interacción del usuario.

        Returns:
            str: Nombre del botón que el usuario seleccionó. Posibles valores:
                'Ok', 'Cancel', 'Yes', 'No', 'Retry', 'Ignore', 'Close'.

        Note:
            Este método bloquea hasta que el usuario interactúa con el diálogo.
        """
        response = self.exec()
        for name, btn in QMessageBox.StandardButton.__members__.items():
            if btn == response:
                return name