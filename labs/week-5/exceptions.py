class CharacterError(Exception):
    """Base exception for all character-related errors."""
    pass


class InvalidLivesError(CharacterError):
    """Raised when lives is outside 0-99."""
    def __init__(self):
        super().__init__("Lives must be between 0 and 99")


class InvalidCoinsError(CharacterError):
    """Raised when coins is outside 0-999."""
    def __init__(self):
        super().__init__("Coins must be between 0 and 999")


class CharacterDeadError(CharacterError):
    """Raised when using a dead character."""
    def __init__(self, name):
        super().__init__(f"{name} has no lives remaining!")