import random

from src.Validations.DataValidation import DataValidation


class SecretCode:
    def __init__(self, secret_code: dict = None):
        positions = [p for p in range(0, 4)]
        if secret_code is None:
            self.__secret_code = {position: random.randint(1, 6) for position in positions}
        else:
            self.__secret_code = secret_code.copy()
            DataValidation.validate_secret_code_dict(secret_code)

    def __str__(self):
        digits = ''
        for digit in self.secret_code.values():
            digits += f'{digit}'
        return digits

    @property
    def secret_code(self):
        return self.__secret_code

    def equal_code(self, other):
        if self.__secret_code == other.secret_code:
            return True
        else:
            return False

    def count_correct_position(self, other):
        count = 0
        for key, value in other.secret_code.items():
            if self.__secret_code[key] == value:
                count += 1
        return count

    def count_incorrect_position(self, other):
        count = 0
        print(self.__str__())
        correct_list = list(self.__secret_code.values())
        hit_list = correct_list.copy()
        # for i in range(4):
        #     if self_values[i] != other_values[i]:
        #         count += 1
        for key, value in other.secret_code.items():
            if value in correct_list:
                if value in hit_list:
                    count += 1
                    hit_list.remove(value)
        for key, value in other.secret_code.items():
            if self.__secret_code[key] == value:
                count -= 1
        return count
