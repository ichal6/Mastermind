class IncorrectSecretCodeError(Exception):
    """Exception raised for error in the secret code

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Secret code is incorrect"):
        self.message = message
