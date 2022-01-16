from abc import ABC, abstractmethod
from src.Models.SecretCode import SecretCode


class GameRule(ABC):
    """
    Abstract class for game's rule. It's parent class for ChetGame and FairGame
    """
    def __init__(self, secret_code: SecretCode):
        """
        Fields
        ----------
        __attempt_number: int
            counter of try
        __MAX_ATTEMPT: int
            max number of try

        Parameters
        ----------
        secret_code: SecretCode
            Secret code generate from computer and assigned to class

        """
        self.__secret_code = secret_code
        self.__attempt_number = 0
        self.__MAX_ATTEMPT = 12

    @abstractmethod
    def check(self, possible_code):
        """
        Check a code from user

        Parameters
        ---------
        possible_code: SecretCode
            code from user.
        """
        raise NotImplementedError

    @abstractmethod
    def get_count_correct_position(self, possible_code) -> int:
        """
        Return correct position value

        Parameters
        -----------
        possible_code: SecretCode
            code from user
        """
        raise NotImplementedError

    @property
    def attempt_number(self):
        return self.__attempt_number

    @property
    def secret_code(self):
        return self.__secret_code

    def max_attempt(self):
        """
        Return MAX_ATTEMPT value
        """
        return self.__MAX_ATTEMPT

    def increase_attempt_number(self):
        """
        increment counter of try
        """
        self.__attempt_number += 1

    def get_count_incorrect_position(self, possible_code) -> int:
        """
        Return incorrect position number

        Parameters
        -----------
        possible_code: SecretCode
            code from user
        """
        raise NotImplementedError

    def get_code_value(self) -> str:
        """
        Convert code generate from computer to str
        """
        return str(self.__secret_code)
