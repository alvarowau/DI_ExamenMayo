class Validation:
    """Clase utilitaria para validación de datos de entrada.

    Proporciona métodos estáticos para validar diferentes tipos de datos comunes:
    - Campos vacíos
    - Números
    - Emails
    - Teléfonos
    - DNIs españoles
    """

    @staticmethod
    def is_empty(text: str) -> bool:
        """Verifica si un texto está vacío o contiene solo espacios.

        Args:
            text (str): Texto a validar.

        Returns:
            bool: True si el texto es None, vacío o solo espacios en blanco.
        """
        return text is None or text.strip() == ''

    @staticmethod
    def is_numeric(text: str) -> bool:
        """Verifica si un texto contiene solo caracteres numéricos.

        Args:
            text (str): Texto a validar.

        Returns:
            bool: True si el texto contiene solo dígitos, False en caso contrario.
        """
        return text.isdigit() if text else False

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Realiza una validación básica de formato de email.

        Args:
            email (str): Dirección de email a validar.

        Returns:
            bool: True si contiene '@' y '.', False si está vacío o no cumple formato.
        """
        if Validation.is_empty(email):
            return False
        return '@' in email and '.' in email

    @staticmethod
    def is_phone_number(text: str) -> bool:
        """Valida si un texto podría ser un número de teléfono.

        Args:
            text (str): Texto a validar.

        Returns:
            bool: True después de eliminar espacios y guiones, si lo que queda son solo dígitos.
        """
        return text.replace(" ", "").replace("-", "").isdigit() if text else False

    @staticmethod
    def is_valid_dni(dni: str) -> bool:
        """Valida un DNI español según formato oficial (8 números + letra de control).

        Args:
            dni (str): DNI a validar.

        Returns:
            bool: True si cumple con el formato y la letra es correcta.

        Note:
            La letra se calcula como el resto de dividir el número entre 23,
            usando la secuencia 'TRWAGMYFPDXBNJZSQVHLCKE' para la correspondencia.
        """
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9:
            return False
        num_part = dni[:8]
        letter = dni[-1].upper()
        if not num_part.isdigit() or not letter.isalpha():
            return False
        return letras[int(num_part) % 23] == letter