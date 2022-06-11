from datetime import datetime
from os.path import exists
import sys

from src.Databases.Dao import Dao
from src.Models.Result import Result


def e_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class CSVDao(Dao):
    def __init__(self, filename='winner.txt'):
        self.file_with_score = filename

    def save_result(self, name: str, attempt_number: int, date: datetime):
        with open(self.file_with_score, 'a') as f:
            f.write(name + ' ' + str(attempt_number) + ' ' + str(datetime.timestamp(date)) + '\n')

    def get_results(self):
        results = []
        file_exists = exists(self.file_with_score)
        if not file_exists:
            return results
        with open(self.file_with_score) as f:
            lines = f.readlines()
        for line in lines:
            line = line.split(" ")
            try:
                result = Result(line[0], int(line[1]), datetime.fromtimestamp(float(line[2])))
                results.append(result)
            except ValueError as e:
                e_print(str(e))
        return results
