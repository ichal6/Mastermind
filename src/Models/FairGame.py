from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode


class FairGame(GameRule):
    """
    Class for play a fair game.
    """
    def __init__(self, secret_code):
        super().__init__(secret_code)

    def check(self, possible_code: SecretCode) -> bool:
        """
        This method compare code generate from computer with code input from user.
        If the same return True, if not return False
        Increment attempt counter

        Parameters
        ---------
        possible_code: SecretCode
            code from user.
        """
        self.increase_attempt_number()
        return self.secret_code.equal_code(possible_code) if True else False

    def get_count_correct_position(self, possible_code: SecretCode) -> int:
        """
        This method calculate count of correct position.

        Parameters
        -----------
        possible_code: SecretCode
            code from user
        """
        return self.secret_code.count_correct_position(possible_code)

    def get_count_incorrect_position(self, possible_code: SecretCode) -> int:
        """
        This method calculate count of incorrect position.

        Parameters
        -----------
        possible_code: SecretCode
            code from user
        """
        return self.secret_code.count_incorrect_position(possible_code)
