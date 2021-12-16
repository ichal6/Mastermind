import random


class SecretCode:
    def __init__(self, secret_code: dict = None):
        self.__secret_code = dict() if secret_code is None else secret_code.copy()
        if secret_code is None:
            for number in range(0, 4):
                self.__secret_code[number] = random.randint(1, 6)

    @property
    def secret_code(self):
        return self.__secret_code

    def equal_code(self, other: dict):
        if self.__secret_code == other:
            return True
        else:
            return False
