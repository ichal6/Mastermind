from src.Models.RegulyGry import RegulyGry
from src.Models.SecretCode import SecretCode


class FairGame(RegulyGry):
    def __init__(self, secret_code):
        super().__init__(secret_code)

    def check(self, possible_code: SecretCode) -> bool:
        if not self._secret_code.equal_code(possible_code.secret_code):
            return False
