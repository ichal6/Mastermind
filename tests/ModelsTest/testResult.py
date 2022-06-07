import datetime
from unittest import TestCase

from src.Models.Result import Result


class TestResult(TestCase):
    def test_1_create_result_object_and_return_name(self):
        # given
        name = 'Mike'

        # when
        result = Result(name, 3)

        # then
        self.assertEqual(name, result.get_name())

    def test_2_create_result_object_and_return_attempt_number(self):
        # given
        name = 'Mike'
        attempt = 3

        # when
        result = Result(name, attempt)

        # then
        self.assertEqual(attempt, result.get_attempt())

    def test_3_create_result_object_with_specific_date_and_return_this_date(self):
        # given
        name = 'Mike'
        attempt = 3
        date = datetime.datetime(2022, 6, 7, 13, 26)

        # when
        result = Result(name, attempt, date)

        # then
        self.assertEqual(date, result.get_date())

    def test_4_create_result_object_without_date_and_return_now_date(self):
        # given
        name = 'Mike'
        attempt = 3
        date = datetime.datetime.now()

        # when
        result = Result(name, attempt)

        t = result.get_date() - date

        # then
        self.assertAlmostEqual(date.timestamp(), result.get_date().timestamp(), None, None, delta=60)
