import unittest
from src.Models.FairGame import FairGame
from src.Models.SecretCode import SecretCode


def print_secret_code(secret_code: dict):
    for digit in secret_code.values():
        print(digit, end="")


def generate_wrong_answer(secret_code: dict):
    answer = dict()

    for item in secret_code.items():
        if item[1] != 6:
            answer[item[0]] = item[1] + 1
        else:
            answer[item[0]] = item[1] - 1

    return answer


class MainTest(unittest.TestCase):
    def test_1_should_display_secret_code_and_return_error_message_if_insert_wrong_code(self):
        # given
        secret_code = SecretCode()
        wrong_code = generate_wrong_answer(secret_code.secret_code)
        game = FairGame(secret_code)
        # when
        is_win = secret_code.equal_code(wrong_code)
        # then
        print("Secret code: ", end="")
        print_secret_code(secret_code.secret_code)
        print("\nAnswer: ", end="")
        print_secret_code(wrong_code)
        print("", end="", flush=True)

        self.assertIs(is_win, False)
