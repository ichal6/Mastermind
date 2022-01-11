from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode


class CheatGame(GameRule):
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
        self.increase_attempt_number()
        return False

    def get_count_correct_position(self, possible_code: SecretCode) -> int:
        for value in self.__generator_c_p:
            return value

    def get_count_incorrect_position(self, possible_code: SecretCode) -> int:
        for value in self.__generator_i_p:
            return value
