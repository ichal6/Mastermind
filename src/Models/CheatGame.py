from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode


class CheatGame(GameRule):
    """
    A class for unfair game. It's inherit from GameRule

    Attributes
    ----------
    __generator_c_p: generator
        a generate fake number of correct position. Use max attempts and modulo
    __generator_i_p: generator
        a generate fake number of incorrect position. Use secret code (for base) and modulo
    """
    def __init__(self, secret_code):
        """
        Initialize false rule for game.
        Initialize list comprehensions from secret code (multiply by 3) and max_attempt.
        (for correct position and incorrect position). In the next step initialize generators
        (generator_c_p - correct pos. and generator_i_p - incorrect pos.)

        Parameters
        ----------
        secret_code : SecretCode
            Random SecretCode
        """
        super().__init__(secret_code)

        secret_code_list = [int(n) for n in str(secret_code)] * 3
        last_index = len(secret_code_list) - 1
        list_for_generator = [secret_code_list[i] for i in range(last_index, -1, -1)]

        self.__generator_c_p = (i % 4 for i in range(self.max_attempt()))
        self.__generator_i_p = (i % 4 for i in list_for_generator)

    def check(self, possible_code: SecretCode) -> bool:
        """
        Increment attempt counter and return false

        Parameters
        ----------
        possible_code: SecretCode
          secret code for check
        """
        self.increase_attempt_number()
        return False

    def get_count_correct_position(self, possible_code: SecretCode) -> int:
        """
        Use generator for return correct position value. Ignore code from user
        """
        for value in self.__generator_c_p:
            return value

    def get_count_incorrect_position(self, possible_code: SecretCode) -> int:
        """
        Use generator for return incorrect position value. Ignore code from user
        """
        for value in self.__generator_i_p:
            return value
