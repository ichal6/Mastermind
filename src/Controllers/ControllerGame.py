from src.Models.RuleGame import RegulyGry
from src.Models.SecretCode import SecretCode
from src.Views.View import View


class ControllerGame:
    def __init__(self, game_rule: RegulyGry, view: View):
        self.__game = game_rule
        self.__view = view

    def check(self, possible_code: SecretCode):
        count_correct_positions = self.__game.get_count_correct_position(possible_code)
        self.__view.answer(possible_code, count_correct_positions, 0)
