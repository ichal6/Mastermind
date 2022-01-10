from abc import ABC, abstractmethod


class View(ABC):
    def __init__(self):
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def is_cheater(self):
        is_cheater = self.controller.is_cheater()
        secret_code_as_str = self.controller.display_code()

        if is_cheater:
            self.__cheat_game_message()
        else:
            self.__fair_game_message(secret_code_as_str)

    @abstractmethod
    def answer(self, provide_code, count_correct_number, count_incorrect_position):
        raise NotImplementedError

    @abstractmethod
    def win(self):
        raise NotImplementedError

    @abstractmethod
    def game_over(self):
        raise NotImplementedError

    @abstractmethod
    def check_button_clicked(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def __fair_game_message(secret_code: str):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def __cheat_game_message():
        raise NotImplementedError
