import unittest

from src.Models.SecretCode import SecretCode
from tests.CommonUse import generate_secret_code, generate_wrong_answer


class MainTest(unittest.TestCase):
    def test_1_should_create_with_default_secret_code(self):
        # given
        given_code = generate_secret_code()
        # when
        secret_code = SecretCode(given_code)
        # then
        self.assertEqual(secret_code.secret_code, given_code)

    def test_2_should_create_with_random_secret_code(self):
        # given
        size_of_code = 4

        # when
        secret_code = SecretCode()

        # then
        self.assertIsNotNone(secret_code.secret_code)
        self.assertEqual(len(secret_code.secret_code), size_of_code)

    def setUp(self) -> None:
        self.given_code = {
            1: 6,
            2: 5,
            3: 4,
            4: 3
        }
        self.code_as_string = '6543'
        self.secret_code = SecretCode(self.given_code)

    def test_3_should_return_code_as_string(self):
        # given
        # when
        digits = self.secret_code.__str__()

        # then
        self.assertEqual(self.code_as_string, digits)

    def test_4_should_return_zero_correct_positions(self):
        # given
        wrong_code = SecretCode(generate_wrong_answer(self.secret_code.secret_code))

        # when
        value = self.secret_code.count_correct_position(wrong_code)

        # then
        self.assertEqual(value, 0)

    def test_5_should_return_three_correct_positions(self):
        # given
        self.given_code[1] = 1
        wrong_code = SecretCode(self.given_code)

        # when
        value = self.secret_code.count_correct_position(wrong_code)

        # then
        self.assertEqual(3, value)

    def test_6_should_return_four_correct_positions(self):
        # given
        wrong_code = SecretCode(self.given_code)

        # when
        value = self.secret_code.count_correct_position(wrong_code)

        # then
        self.assertEqual(4, value)

    def test_7_should_return_two_correct_positions(self):
        # given
        self.given_code[1] = 1
        self.given_code[2] = 2
        wrong_code = SecretCode(self.given_code)

        # when
        value = self.secret_code.count_correct_position(wrong_code)

        # then
        self.assertEqual(2, value)


if __name__ == '__main__':
    unittest.main()
