from abc import ABC, abstractmethod


class View(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def answer(self, provide_code, count_correct_number, count_incorrect_position):
        raise NotImplementedError

    @abstractmethod
    def win(self):
        raise NotImplementedError

    @abstractmethod
    def game_over(self):
        raise NotImplementedError
