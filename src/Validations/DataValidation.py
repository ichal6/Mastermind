from src.Exceptions.IncorrectSecretCodeError import IncorrectSecretCodeError


class DataValidation:
    """
    A class for validate data
    """

    @staticmethod
    def validate_secret_code_dict(possible_secret_code: dict):
        """
        Parameters
        ----------
        possible_secret_code : dict
            Secret code for check data format
        """

        for key, value in possible_secret_code.items():
            if key in range(0, 4):
                if value not in range(1, 7):
                    raise IncorrectSecretCodeError("Value is incorrect")
            else:
                raise IncorrectSecretCodeError("Key is incorrect")
       