import sqlite3
import pytz

from datetime import datetime


class DB:
    """
    This class is used as the parent class for sqlite3 database methods
    """

    def __init__(self, dbpath: str, timezone='UTC'):
        """
        Args:
            dbpath (str): path to database file
            timezone (str, optional): database timezone. Defaults to 'UTC'.
        """
        self.dbpath = dbpath
        self.timezone = timezone

    def connect(self) -> sqlite3.Connection:
        """
        Returns:
            sqlite3.Connection: creates connection to database
        """
        con = sqlite3.connect(self.dbpath)
        con.row_factory = self.dictFactory
        return con

    def getCurrentDate(self) -> str:
        """
        Returns:
            str: current date in sql format
        """
        return self.getTimezoneDate().strftime('%Y-%m-%d %H:%M:%S')

    def getTimezoneDate(self) -> datetime:
        """
        Returns:
            datetime: localtime according to timezone attribute
        """
        time = datetime.utcnow()

        utcTz = pytz.timezone('UTC')
        localTz = pytz.timezone(self.timezone)

        utcTime = time.replace(tzinfo=utcTz)
        localTime = utcTime.astimezone(localTz)

        return localTime

    @staticmethod
    def dictFactory(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
        """
        Args:
            cursor (sqlite3.Cursor): cursor
            row (sqlite3.Row): row

        Returns:
            dict: row factory for sqlite3.Connection
        """
        save_dict = {}

        for idx, col in enumerate(cursor.description):
            save_dict[col[0]] = row[idx]

        return save_dict

    @staticmethod
    def updateFormat(sql: str, parameters: dict) -> tuple[str, list]:
        """
        Args:
            sql (str): sql string
            parameters (dict): 'update' query parameters

        Returns:
            tuple[str, list]:
                formatted 'update' query parameters for sqlite3.execute
        """
        values = ", ".join([
            f"{item} = ?" for item in parameters
        ])
        sql += f" {values}"

        return sql, list(parameters.values())

    @staticmethod
    def updateFormatWhere(sql, parameters: dict) -> tuple[str, list]:
        """
        Args:
            sql (_type_): sql string
            parameters (dict): 'where' query parameters

        Returns:
            tuple[str, list]:
                formatted 'where' query parameters for sqlite3.execute
        """
        if not parameters:
            return sql, list()

        sql += " WHERE "

        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])

        return sql, list(parameters.values())
