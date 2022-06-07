from abc import ABC, abstractmethod


class Dao(ABC):
    """
    An abstract class used to save result to databases
    """

    @abstractmethod
    def save_result(self, name: str, attempt_number: int):
        raise NotImplementedError

    @abstractmethod
    def get_results(self):
        raise NotImplementedError
