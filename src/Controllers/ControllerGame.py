from src.Models.CheatGame import CheatGame
from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode
from src.Services.GameService import GameService
from src.Views.View import View


class ControllerGame:
    def __init__(self, game_rule: GameRule, view: View):
        self.__game = game_rule
        self.__view = view

    def check(self, possible_code: SecretCode):
        count_correct_positions = self.__game.get_count_correct_position(possible_code)
        count_incorrect_positions = self.__game.get_count_incorrect_position(possible_code)
        is_win = self.__game.check(possible_code)
        self.__view.answer(possible_code, count_correct_positions, count_incorrect_positions)
        if is_win:
            self.__view.win()
        if self.__game.attempt_number > self.__game.max_attempt():
            self.__view.game_over()

    def check_from_string(self, secret_code_raw: str):
        possible_secret_code = GameService.build_secret_code(secret_code_raw)
        self.check(possible_secret_code)

    def is_cheater(self):
        return isinstance(self.__game, CheatGame)

    def display_code(self) -> str:
        return self.__game.get_code_value()

    def reset(self):
        self.__game = GameService.build_game_rule()
