from unittest import TestCase

from src.Models.FairGame import FairGame
from src.Models.SecretCode import SecretCode
from tests.CommonUse import generate_secret_code, generate_wrong_answer


class TestFairGame(TestCase):

    __secret_code = None

    @classmethod
    def setUpClass(cls) -> None:
        secret_code_dict = generate_secret_code()
        cls.__secret_code = SecretCode(secret_code_dict)
        cls.__fair_game = FairGame(cls.__secret_code)

    def test_1_should_return_true_when_code_is_the_same(self):
        # given
        # when
        is_the_same = self.__fair_game.check(self.__secret_code)
        # then
        self.assertTrue(is_the_same)

    def test_2_should_return_false_when_code_is_not_the_same(self):
        # given
        wrong_code = SecretCode(generate_wrong_answer(self.__secret_code.secret_code))
        # when
        is_the_same = self.__fair_game.check(wrong_code)
        # then
        self.assertIs(is_the_same, False)

    def test_3_should_return_info_about_nothing_guess(self):
        # given
        wrong_code = SecretCode(generate_wrong_answer(self.__secret_code.secret_code))
        exp_value = 0
        # when
        return_value = self.__fair_game.get_count_correct_position(wrong_code)
        # then
        self.assertEqual(exp_value, return_value)
