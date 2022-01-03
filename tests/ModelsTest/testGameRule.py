from unittest import TestCase
from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode
from tests.CommonUse import generate_secret_code, generate_wrong_answer


class TestGameRule(TestCase):
    __secret_code = None

    @classmethod
    def setUpClass(cls) -> None:
        GameRule.__abstractmethods__ = set()
        secret_code_dict = generate_secret_code()
        cls.__secret_code = SecretCode(secret_code_dict)
        cls.__game = GameRule(cls.__secret_code)

    def test_increase_attempt_number_by_one(self):
        # given
        # when
        self.__game.increase_attempt_number()
        # then
        self.assertEqual(self.__game._GameRule__attempt_number, 1)
