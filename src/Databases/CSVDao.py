from datetime import datetime

from src.Databases.Dao import Dao


class CSVDao(Dao):
    def __init__(self, filename='winner.txt'):
        self.file_with_score = filename

    def save_result(self, name: str, attempt_number: int, date: datetime):
        with open(self.file_with_score, 'a') as f:
            f.write(name + ' ' + str(attempt_number) + ' ' + str(date) + '\n')

    def get_results(self):
        with open(self.file_with_score) as f:
            lines = f.readlines()
        return lines
