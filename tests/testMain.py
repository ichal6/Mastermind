import unittest
from src.Models.FairGame import FairGame
from src.Models.SecretCode import SecretCode
from tests.CommonUse import generate_wrong_answer, print_secret_code


class MainTest(unittest.TestCase):
    def test_1_should_display_secret_code_and_return_error_message_if_insert_wrong_code(self):
        # given
        secret_code = SecretCode()
        wrong_code = generate_wrong_answer(secret_code.secret_code)
        game = FairGame(secret_code)
        # when
        is_the_same = secret_code.equal_code(wrong_code)
        is_win = game.check(SecretCode(wrong_code))
        # then
        print("Secret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("\nAnswer: ", end="")
        print_secret_code(wrong_code)
        print("", end="", flush=True)

        self.assertIs(is_the_same, False)
        self.assertIs(is_win, False)


if __name__ == '__main__':
    unittest.main()
