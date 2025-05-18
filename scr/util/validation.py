class Validation:
    """Clase con métodos estáticos para validar datos de entrada."""

    @staticmethod
    def is_empty(text: str) -> bool:
        """Devuelve True si el texto es None, vacío o solo espacios."""
        return text is None or text.strip() == ''

    @staticmethod
    def is_numeric(text: str) -> bool:
        """Devuelve True si el texto contiene solo números."""
        return text.isdigit() if text else False

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Valida si el texto tiene formato de email simple."""
        if Validation.is_empty(email):
            return False
        return '@' in email and '.' in email

    @staticmethod
    def is_phone_number(text: str) -> bool:
        """Devuelve True si el texto parece un número de teléfono."""
        return text.replace(" ", "").replace("-", "").isdigit() if text else False

    @staticmethod
    def is_valid_dni(dni: str) -> bool:
        """Valida si el texto es un DNI español correcto (8 números + letra válida)."""
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9:
            return False
        num_part = dni[:8]
        letter = dni[-1].upper()
        if not num_part.isdigit() or not letter.isalpha():
            return False
        return letras[int(num_part) % 23] == letter
