from abc import ABC, abstractmethod


class View(ABC):
    def __init__(self):
        self.__controller = None

    def set_controller(self, controller):
        self.__controller = controller

    @property
    def controller(self):
        return self.__controller

    def is_cheater(self):
        is_cheater = self.__controller.is_cheater()
        secret_code_as_str = self.__controller.display_code()

        if is_cheater:
            self.__cheat_game_message()
            self.reset()
            return True
        else:
            self.__fair_game_message(secret_code_as_str)
            self.reset()
            return False

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

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def __fair_game_message(secret_code: str):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def __cheat_game_message():
        raise NotImplementedError
