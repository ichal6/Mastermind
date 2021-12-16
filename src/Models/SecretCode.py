import random


class SecretCode:
    def __init__(self):
        self.__secret_code = dict()
        for number in range(0, 4):
            self.__secret_code[number] = random.randint(1, 6)

    @property
    def secret_code(self):
        return self.__secret_code

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass