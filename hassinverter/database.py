from typing import List
import mysql.connector
from mysql.connector.connection import MySQLConnection

from hassinverter.config import get_config

import logging
_LOGGER = logging.getLogger(__name__)

_config = get_config()


class Database:
    _db: MySQLConnection

    def __init__(self) -> None:
        self._db = mysql.connector.connect(
            host=_config["mysql"]["host"],
            user=_config["mysql"]["user"],
            password=_config["mysql"]["password"],
            database=_config["mysql"]["database"]
        )

    def get_last_record(self, inverter: str):
        self._db.commit()
        cursor = self._db.cursor(
            dictionary=True, buffered=False, prepared=False)

        cursor.execute(
            f"SELECT * FROM `{inverter}` ORDER BY `time` DESC LIMIT 1")
        return cursor.fetchall()[0]

    def get_inverters(self) -> List[str]:
        cursor = self._db.cursor()
        cursor.execute("SHOW TABLES")

        return [
            x[0] for x in cursor
        ]
