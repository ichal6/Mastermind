from src.Models.SecretCode import SecretCode


class RegulyGry:
    def __init__(self, secret_code: SecretCode):
        self._secret_code = secret_code

    def check(self, possible_code):
        pass
