from datetime import datetime
from unittest import TestCase

from src.Databases.CSVDao import CSVDao


class TestCSVDao(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.FILENAME = '../test_score.txt'
        cls.FILE_BAD = '../test_score_wrong.txt'

    def test_0_should_return_empty_result_list(self):
        # given
        # when
        dao = CSVDao(self.FILENAME)
        results = dao.get_results()

        # then
        self.assertEqual(0, len(results))

    def test_1_should_ignore_entry_if_result_in_file_is_incorrect(self):
        # given
        name = "Jola"
        wrong_data = "s"
        with open(self.FILE_BAD, 'a') as f:
            f.write(name + ' ' + wrong_data + '\n')

        # when
        dao = CSVDao(self.FILE_BAD)
        results = dao.get_results()

        # then
        self.assertEqual(0, len(results))

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

        entry = name + ' ' + str(attempt_number) + ' ' + str(datetime.timestamp(date)) + '\n'
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
        results = dao.get_results()

        # then
        self.assertEqual(1, len(results))
        self.assertEqual(name, results[0].get_name())
        self.assertEqual(attempt_number, results[0].get_attempt())
        self.assertEqual(date, results[0].get_date())

    @classmethod
    def tearDownClass(cls):
        open(cls.FILENAME, 'w').close()
