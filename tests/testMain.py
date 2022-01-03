import unittest

from src.Controllers.ControllerGame import ControllerGame
from src.Models.FairGame import FairGame
from src.Models.SecretCode import SecretCode
from src.Views.ConsoleView import ConsoleView
from tests.CommonUse import generate_wrong_answer, print_secret_code, mixed_up_answer


class MainTest(unittest.TestCase):
    def test_1_should_display_secret_code_and_return_error_message_if_insert_wrong_code(self):
        # given
        secret_code = SecretCode({0: 5, 1: 4, 2: 3, 3: 4})
        wrong_code_dict = generate_wrong_answer(secret_code.secret_code)
        wrong_code = SecretCode(wrong_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        # when
        is_the_same = secret_code.equal_code(wrong_code)
        is_win = game.check(wrong_code)
        number_of_correct_position = game.get_count_correct_position(wrong_code)
        # then
        print("\nWylosowany secret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        controller.check(wrong_code)

        self.assertIs(is_the_same, False)
        self.assertIs(is_win, False)
        self.assertEqual(0, number_of_correct_position)

    def test_2_should_display_secret_code_and_return_incorrect_position_message_if_insert_mixed_code(self):
        # given
        secret_code = SecretCode({0: 5, 1: 4, 2: 3, 3: 4})
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)

        mixed_position_code_dir = mixed_up_answer(secret_code.secret_code)
        mixed_position_code = SecretCode(mixed_position_code_dir)
        # when
        number_of_incorrect_position = game.get_count_incorrect_position(mixed_position_code)

        # then
        print("\nWylosowany secret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        controller.check(mixed_position_code)

        self.assertEqual(4, number_of_incorrect_position)


if __name__ == '__main__':
    unittest.main()
