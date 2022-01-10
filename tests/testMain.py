import unittest

from src.Controllers.ControllerGame import ControllerGame
from src.Exceptions.IncorrectSecretCodeError import IncorrectSecretCodeError
from src.Models.CheatGame import CheatGame
from src.Models.FairGame import FairGame
from src.Models.SecretCode import SecretCode
from src.Views.ConsoleView import ConsoleView
from tests.CommonUse import generate_wrong_answer, print_secret_code, mixed_up_answer, generate_secret_code, \
    convert_dict_secret_code_to_string


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

    def test_3_should_return_two_hit_and_two_mishit(self):
        # given
        secret_code = SecretCode({0: 5, 1: 4, 2: 3, 3: 4})
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)

        half_correct_code = SecretCode({0: 5, 1: 3, 2: 4, 3: 4})
        # when
        number_of_incorrect_position = game.get_count_incorrect_position(half_correct_code)
        number_of_correct_position = game.get_count_correct_position(half_correct_code)

        # then
        print("\nWylosowany secret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        controller.check(half_correct_code)

        self.assertEqual(2, number_of_incorrect_position)
        self.assertEqual(2, number_of_correct_position)

    def test_4_should_win_when_insert_correct_code(self):
        # given
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)

        hit_correct_code = SecretCode(secret_code_dict)
        # when
        number_of_incorrect_position = game.get_count_incorrect_position(hit_correct_code)
        number_of_correct_position = game.get_count_correct_position(hit_correct_code)
        is_win = game.check(hit_correct_code)

        # then
        print("\nWylosowany secret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        controller.check(hit_correct_code)

        self.assertEqual(0, number_of_incorrect_position)
        self.assertEqual(4, number_of_correct_position)
        self.assertIs(is_win, True)

    def test_5_should_display_game_over_message_after_12_attempts(self):
        # given
        secret_code_dict = generate_secret_code()
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)

        wrong_code = SecretCode(generate_wrong_answer(secret_code_dict))
        # when
        is_win = game.check(wrong_code)

        # then
        print("\nWylosowany secret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        for count in range(1, 13):
            print('\nPróba numer: ', count)
            controller.check(wrong_code)

        self.assertIs(is_win, False)

    def test_6_should_disregard_code_if_format_is_incorrect(self):
        # given
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)

        # when
        view.check_button_clicked("1234")
        with self.assertRaises(IncorrectSecretCodeError):
            view.check_button_clicked("asds")
        with self.assertRaises(IncorrectSecretCodeError):
            view.check_button_clicked("0892")
        with self.assertRaises(IncorrectSecretCodeError):
            view.check_button_clicked("-1234")
        with self.assertRaises(IncorrectSecretCodeError):
            view.check_button_clicked("12")
        with self.assertRaises(IncorrectSecretCodeError):
            view.check_button_clicked("123456")
        view.check_button_clicked("1234")
        # then
        self.assertEqual(2, game.attempt_number)

    def test_7_should_display_tere_fere_if_rule_is_fair(self):
        # given
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)

        # when
        # then
        view.is_cheater()

    def test_8_should_display_info_about_cheat_if_rule_is_cheat(self):
        # given
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = CheatGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)

        # when
        # then
        view.is_cheater()

    def test_9_should_can_reset_the_game(self):
        # given
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = CheatGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)

        # when
        for _ in range(10):
            view.check_button_clicked("1234")
        view.reset()
        wrong_answer = generate_wrong_answer(controller._ControllerGame__game._secret_code.secret_code)
        wrong_answer_dict = convert_dict_secret_code_to_string(wrong_answer)
        for _ in range(5):
            view.check_button_clicked(wrong_answer_dict)
        # then
        self.assertEqual(5, controller._ControllerGame__game.attempt_number)


if __name__ == '__main__':
    unittest.main()
