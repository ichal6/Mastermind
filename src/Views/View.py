from abc import ABC, abstractmethod


class View(ABC):
    """
    An abstract class used to interaction with user

    Attributes
    ----------
    __controller: ControllerGame
        controller use to manipulate with data in program
    """
    def __init__(self):
        self.__controller = None

    def set_controller(self, controller):
        """
        Method used to set a controller
        """
        self.__controller = controller

    @property
    def controller(self):
        return self.__controller

    def is_cheater(self):
        """
        Method use for check the rule game.
        Display correspondent communicate for particular rule:
        Cheat game message or fair game message.
        After display message reset a game
        """
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
        """
        Method use for display answer

        Parameters
        ----------
        provide_code: int
            the last provide code from user
        count_correct_number: int
        count_incorrect_position: int
        """
        raise NotImplementedError

    @abstractmethod
    def win(self):
        """
        Display win message
        """
        raise NotImplementedError

    @abstractmethod
    def game_over(self):
        """
        Display lose game message
        """
        raise NotImplementedError

    @abstractmethod
    def check_button_clicked(self):
        """
        Get a code from user and send it to controller
        """
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        """
        Use a controller for reset a game
        """
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
        """
        Display info: It was a fair game rule and show a code
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def __cheat_game_message():
        """
        Display info: It's not a fair game.
        """
        raise NotImplementedError
