from src.Models.RegulyGry import RegulyGry
from src.Models.SecretCode import SecretCode


class FairGame(RegulyGry):
    def __init__(self, secret_code):
        super().__init__(secret_code)
    # Klasa nadrzedna posiada secret code jako pole prywatne
    def check(self, possible_code: SecretCode) -> bool:
        pass

