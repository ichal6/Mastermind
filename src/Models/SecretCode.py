import random


class SecretCode:
    def __init__(self, secret_code: dict = None):
        self.__secret_code = dict() if secret_code is None else secret_code.copy()
        if secret_code is None:
            for number in range(0, 4):
                self.__secret_code[number] = random.randint(1, 6)

    def __str__(self):
        digits = ''
        for digit in self.secret_code.values():
            digits += f'{digit}'
        return digits

    @property
    def secret_code(self):
        return self.__secret_code

    def equal_code(self, other: dict):
        if self.__secret_code == other:
            return True
        else:
            return False

    def count_correct_position(self, other: dict):
        count = 0
        for key, value in other.items():
            if self.__secret_code[key] == value:
                count += 1
        return count
