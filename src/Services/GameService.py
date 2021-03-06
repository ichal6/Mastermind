import random

from src.Exceptions.IncorrectSecretCodeError import IncorrectSecretCodeError
from src.Models import RuleGame, FairGame, CheatGame
from src.Models.SecretCode import SecretCode


class GameService:
    """
    A class for service data
    """

    @staticmethod
    def __convert(string) -> list:
        """
        Convert from string to list

        Parameters
        ----------
        string : str
            Code for convert to list

        Returns
        -----------
        list1
            a list of single elements slices from string
        """
        list1 = []
        list1[:0] = string
        return list1

    @staticmethod
    def build_secret_code(secret_code_raw: str) -> SecretCode:
        """
        Generate object Secret Code from raw str

        Parameters
        ----------
        secret_code_raw : str
            Code for convert to SecretCode

        Returns
        -----------
        SecretCode
            a SecretCode object from str
        """
        code_list = GameService.__convert(secret_code_raw)
        if len(code_list) != 4:
            raise IncorrectSecretCodeError("Wrong size of code")
        try:
            positions = [p for p in range(0, 4)]
            code_dict = {position: int(code_list[position]) for position in positions}
            return SecretCode(code_dict)
        except IndexError:
            raise IncorrectSecretCodeError("Too short code")
        except ValueError:
            raise IncorrectSecretCodeError("Not an integer number in code")

    @staticmethod
    def build_game_rule() -> RuleGame:
        """
        Generate and build derived class from RuleGame

        Returns
        -----------
        Subclass of GameRule
        """
        secret_code = SecretCode()
        game_rule = random.choice([CheatGame.CheatGame, FairGame.FairGame])
        game = game_rule(secret_code)

        return game
