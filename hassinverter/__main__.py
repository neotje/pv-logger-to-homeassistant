import sys
from time import sleep

from hassinverter.mqtt import publish_config, publish_state
from hassinverter.config import check_config
from hassinverter.database import Database

import logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(levelname)s:%(name)s:%(funcName)s:[%(lineno)d]   %(message)s'
)
_LOGGER = logging.getLogger(__name__)


def main():
    check_config()

    db = Database()

    inverters = db.get_inverters()

    for i in inverters:
        publish_config(i)

    try:
        while True:
            for i in inverters:
                publish_state(i, db.get_last_record(i))

            sleep(60)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    sys.exit(main())
