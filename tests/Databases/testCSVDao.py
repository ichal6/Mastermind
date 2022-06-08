from datetime import datetime
from unittest import TestCase

from src.Databases.CSVDao import CSVDao


class TestCSVDao(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.FILENAME = '../test_score.txt'

    def test_1_should_return_create_new_entry(self):
        # given
        name = 'Mike'
        attempt_number = 3
        date = datetime(2022, 6, 8, 17, 26, 22, 123456)

        # when
        dao = CSVDao(self.FILENAME)
        dao.save_result(name, attempt_number, date)

        with open(self.FILENAME) as f:
            lines = f.readlines()

        entry = name + ' ' + str(attempt_number) + ' ' + str(date) + '\n'
        expected_output = [entry]

        # then
        self.assertEqual(expected_output, lines)

    def test_2_should_return_result_list(self):
        # given
        name = 'Mike'
        attempt_number = 3
        date = datetime(2022, 6, 8, 17, 26, 22, 123456)

        # when
        dao = CSVDao(self.FILENAME)
        lines = dao.get_results()

        entry = name + ' ' + str(attempt_number) + ' ' + str(date) + '\n'
        expected_output = [entry]

        # then
        self.assertEqual(expected_output, lines)

    @classmethod
    def tearDownClass(cls):
        open(cls.FILENAME, 'w').close()
