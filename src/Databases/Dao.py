from abc import ABC, abstractmethod
from datetime import datetime


class Dao(ABC):
    """
    An abstract class used to save result to databases
    """

    @abstractmethod
    def save_result(self, name: str, attempt_number: int, date: datetime):
        raise NotImplementedError

    @abstractmethod
    def get_results(self):
        raise NotImplementedError
