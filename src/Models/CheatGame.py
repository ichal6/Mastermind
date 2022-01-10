from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode


class CheatGame(GameRule):
    def __init__(self, secret_code):
        super().__init__(secret_code)

    def check(self, possible_code: SecretCode) -> bool:
        self.increase_attempt_number()
        return False

    def get_count_correct_position(self, possible_code: SecretCode) -> int:
        return 0

    def get_count_incorrect_position(self, possible_code: SecretCode) -> int:
        return 4
