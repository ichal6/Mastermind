import unittest

from src.Models.SecretCode import SecretCode
from tests.CommonUse import generate_secret_code


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

    def test_3_should_return_code_as_string(self):
        # given
        given_code = {
            1: 6,
            2: 5,
            3: 4,
            4: 3
        }
        code_as_string = '6543'
        secret_code = SecretCode(given_code)

        # when
        digits = secret_code.__str__()

        # then
        self.assertEqual(code_as_string, digits)


if __name__ == '__main__':
    unittest.main()
