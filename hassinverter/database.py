from typing import List
import mysql.connector

from hassinverter.config import get_config

import logging
_LOGGER = logging.getLogger(__name__)

_config = get_config()
_db = mysql.connector.connect(
    host=_config["mysql"]["host"],
    user=_config["mysql"]["user"],
    password=_config["mysql"]["password"],
    database=_config["mysql"]["database"]
)

def get_last_record(inverter: str):
    _db.commit()
    cursor = _db.cursor(dictionary=True, buffered=False, prepared=False)

    cursor.execute(f"SELECT * FROM `{inverter}` ORDER BY `time` DESC LIMIT 1")
    return cursor.fetchall()[0]

def get_inverters() -> List[str]:
    cursor = _db.cursor()
    cursor.execute("SHOW TABLES")

    return [
        x[0] for x in cursor
    ]