from datetime import datetime


class Result:
    """
    Class for store result of winner
    """
    def __init__(self, name: str, attempt: int, date_of_win: datetime = datetime.now()):
        self.__name = name
        self.__attempt = attempt
        self.__date = date_of_win

    def get_name(self) -> str:
        """
        Get name of winner

        Returns
        -------
        name: str
        """
        return self.__name

    def get_attempt(self) -> int:
        """
        Get count of attempt

        Returns
        -------
        attempt: int
        """
        return self.__attempt

    def get_date(self) -> datetime:
        """
        Get datetime of winner

        Returns
        -------
        date: datetime
        """
        return self.__date
