from src.Exceptions.IncorrectSecretCodeError import IncorrectSecretCodeError
from src.Models.SecretCode import SecretCode


class GameService:
    """
    A class for service data
    """

    @staticmethod
    def __convert(string):
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
    def build_secret_code(secret_code_raw: str):
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
        code_dict = dict()
        try:
            for key in range(0, 4):
                code_dict[key] = int(code_list[key])
        except IndexError:
            raise IncorrectSecretCodeError("Too short code")
        except ValueError:
            raise IncorrectSecretCodeError("Not an integer number in code")

        return SecretCode(code_dict)
