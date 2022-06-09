from datetime import datetime

from src.Databases.CSVDao import CSVDao
from src.Exceptions.IncorrectSecretCodeError import IncorrectSecretCodeError
from src.Models.CheatGame import CheatGame
from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode
from src.Services.GameService import GameService
from src.Views.View import View


class ControllerGame:
    """
    A class used to control behavior of program

    Attributes
    ----------
    __game: GameRule
        rule of game which use in class.
    __view: View
        view use for display information for use (ConsoleView or TkInterView)
    """
    def __init__(self, game_rule: GameRule, view: View):
        """
        Parameters
        ----------
        game_rule: GameRule
            One of two rules of game: FairGame or ChetGame
        view: View
            One of two view: ConsoleView or TkInterView
        """
        self.__game = game_rule
        self.__view = view
        self.__dao = CSVDao()

    def check(self, possible_code: SecretCode):
        """
        This function check a code from user.
        If it is the same as random code generate by computer display a win message.
        If not check a count of attempt and if counter equal max attempts
        display lose message. If not answer attend to list of answers and game is
        continue

        Parameters
        ----------
        possible_code: SecretCode
            Object with code, was input from user
        """
        count_correct_positions = self.__game.get_count_correct_position(possible_code)
        count_incorrect_positions = self.__game.get_count_incorrect_position(possible_code)
        is_win = self.__game.check(possible_code)
        if is_win:
            self.__view.win()
        elif self.__game.attempt_number == self.__game.max_attempt():
            self.__view.game_over()
        else:
            self.__view.answer(possible_code, count_correct_positions, count_incorrect_positions)

    def check_from_string(self, secret_code_raw: str):
        """
        Check the secret code and check the win condition
        ---------
        Parameters
        ---------
        secret_code_raw <- secret code as string
        """
        try:
            possible_secret_code = GameService.build_secret_code(secret_code_raw)
            self.check(possible_secret_code)
        except IncorrectSecretCodeError as error:
            self.__view.show_error(error)

    def is_cheater(self):
        return isinstance(self.__game, CheatGame)

    def display_code(self) -> str:
        return self.__game.get_code_value()

    def reset(self):
        self.__game = GameService.build_game_rule()

    def save_winner(self):
        name_of_winner = self.__view.provide_name("Wygrałeś")
        self.__dao.save_result(name_of_winner, self.__game.attempt_number, datetime.now())

    def get_results(self):
        return self.__dao.get_results()
