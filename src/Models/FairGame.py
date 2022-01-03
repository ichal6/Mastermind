from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode


class FairGame(GameRule):
    def __init__(self, secret_code):
        super().__init__(secret_code)

    def check(self, possible_code: SecretCode) -> bool:
        return self._secret_code.equal_code(possible_code) if True else False

    def get_count_correct_position(self, possible_code: SecretCode) -> int:
        return self._secret_code.count_correct_position(possible_code)
