from abc import ABC, abstractmethod
from src.Models.SecretCode import SecretCode


class GameRule(ABC):
    def __init__(self, secret_code: SecretCode):
        self._secret_code = secret_code
        self.__attempt_number = 0
        self.__MAX_ATTEMPT = 12

    @abstractmethod
    def check(self, possible_code):
        raise NotImplementedError

    @abstractmethod
    def get_count_correct_position(self, possible_code) -> int:
        raise NotImplementedError

    def increase_attempt_number(self):
        self.__attempt_number += 1

    def get_count_incorrect_position(self, possible_code) -> int:
        raise NotImplementedError
