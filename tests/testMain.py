import unittest

from src.Controllers.ControllerGame import ControllerGame
from src.Models.CheatGame import CheatGame
from src.Models.FairGame import FairGame
from src.Models.SecretCode import SecretCode
from src.Views.ConsoleView import ConsoleView
from tests.CommonUse import generate_wrong_answer, print_secret_code, mixed_up_answer, generate_secret_code, \
    convert_dict_secret_code_to_string


class MainTest(unittest.TestCase):
    """
    Główna klasa z testami
    """
    def test_1_should_display_secret_code_and_return_error_message_if_insert_wrong_code(self):
        """
        Wyświetlenie (wypisanie w konsoli) wylosowanego kodu, wpisanie odpowiedzi z błędnymi cyframi
        - oczekiwana informacja o braku poprawnych trafień.
        """
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
        print("\nSecret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        controller.check(wrong_code)

        self.assertIs(is_the_same, False)
        self.assertIs(is_win, False)
        self.assertEqual(0, number_of_correct_position)

    def test_2_should_display_secret_code_and_return_incorrect_position_message_if_insert_mixed_code(self):
        """
        Wyświetlenie wylosowanego kodu, wpisanie odpowiedzi z poprawnymi cyframi w złych miejscach
        - oczekiwana informacja o niepoprawnym położeniu.
        """
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
        print("\nSecret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        controller.check(mixed_position_code)

        self.assertEqual(4, number_of_incorrect_position)

    def test_3_should_return_two_hit_and_two_mishit(self):
        """
        Wyświetlenie wylosowanego kodu, wpisanie odpowiedzi z dwoma poprawnymi cyframi w dobrych miejscach i dwoma poprawnymi w złych miejscach
        - oczekiwana informacja o dwóch trafieniach i dwóch złych pozycjach.
        """
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
        print("\nSecret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        controller.check(half_correct_code)

        self.assertEqual(2, number_of_incorrect_position)
        self.assertEqual(2, number_of_correct_position)

    def test_4_should_win_when_insert_correct_code(self):
        """
        Wyświetlenie wylosowanego kodu, wpisanie poprawnej odpowiedzi
        - oczekiwana informacja o wygranej.

        """
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
        print("\nSecret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        controller.check(hit_correct_code)

        self.assertEqual(0, number_of_incorrect_position)
        self.assertEqual(4, number_of_correct_position)
        self.assertIs(is_win, True)

    def test_5_should_display_game_over_message_after_12_attempts(self):
        """
        Wpisanie 12 razy niepoprawnego kodu - oczekiwana informacja o przegranej
        """
        # given
        secret_code_dict = generate_secret_code()
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)

        wrong_code = SecretCode(generate_wrong_answer(secret_code_dict))

        # when
        print("\nSecret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("", flush=True)
        for count in range(1, 13):
            print('\nPróba numer: ', count)
            view.check_button_clicked(str(wrong_code))

        # then
        self.assertEqual(12, game.attempt_number)

    def test_6_should_disregard_code_if_format_is_incorrect(self):
        """
        Próba wpisania niepoprawnego kodu do pola odpowiedzi (mniej lub więcej niż 4 znaki, znaki nie będące cyframi
         od 1 do 6) - oczekiwane nieuznanie kodu (gracz nie traci tury).
        """
        # given
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)

        # when
        view.check_button_clicked("1234")
        view.check_button_clicked("asds")
        view.check_button_clicked("0892")
        view.check_button_clicked("-1234")
        view.check_button_clicked("12")
        view.check_button_clicked("123456")
        view.check_button_clicked("1234")
        # then
        self.assertEqual(2, game.attempt_number)

    def test_7_should_display_tere_fere_if_rule_is_fair(self):
        """
        Wciśnięcie przycisku „Oszust” przy poprawnych zasadach gry
        - oczekiwana informacja „tere fere”.
        """
        # given
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)

        # when
        is_cheater = view.is_cheater()
        # then
        self.assertEqual(False, is_cheater)

    def test_8_should_display_info_about_cheat_if_rule_is_cheat(self):
        """
        Wciśnięcie przycisku „Oszust” przy niepoprawnych zasadach gry
        - oczekiwana informacja o oszukiwaniu przez komputer.
        """
        # given
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = CheatGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)

        # when
        is_cheater = view.is_cheater()
        # then
        self.assertEqual(True, is_cheater)

    def test_9_should_can_reset_the_game(self):
        """
        Wpisanie 10 kodów, resetowanie gry, wpisanie 5 kodów - oczekiwane normalne działanie gry
        (czy licznik tur resetuje się po wciśnięciu „Reset”).
        """
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
        wrong_answer = generate_wrong_answer(controller._ControllerGame__game.secret_code.secret_code)
        wrong_answer_dict = convert_dict_secret_code_to_string(wrong_answer)
        for _ in range(5):
            view.check_button_clicked(wrong_answer_dict)
        # then
        self.assertEqual(5, controller._ControllerGame__game.attempt_number)

    def test_10_play_game(self):
        """
        Rozegranie próbnej gry w 6 próbach.
        Porównanie stosownej listy nieprawidłowych pozycji do uzyskanej z programu.
        """
        # given
        secret_code_dict = {0: 1, 1: 2, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = ConsoleView()
        controller = ControllerGame(game, view)
        view.set_controller(controller)
        answers = list()
        # when
        answers.append(game.get_count_incorrect_position(SecretCode({0: 6, 1: 6, 2: 2, 3: 2})))
        answers.append(game.get_count_incorrect_position(SecretCode({0: 4, 1: 3, 2: 3, 3: 6})))
        answers.append(game.get_count_incorrect_position(SecretCode({0: 1, 1: 4, 2: 1, 3: 6})))
        answers.append(game.get_count_incorrect_position(SecretCode({0: 3, 1: 3, 2: 4, 3: 6})))
        answers.append(game.get_count_incorrect_position(SecretCode({0: 2, 1: 3, 2: 1, 3: 4})))
        answers.append(game.get_count_incorrect_position(SecretCode({0: 1, 1: 2, 2: 3, 3: 4})))
        # then
        self.assertEqual([1, 1, 1, 2, 3, 0], answers)


if __name__ == '__main__':
    unittest.main()
