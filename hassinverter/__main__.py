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

    publish_config("TOTAL_INVERTERS")

    try:
        while True:
            total = 0
            for i in inverters:
                r = db.get_last_record(i)
                total += r["PAC"]

                publish_state(i, r["PAC"])

            publish_state("TOTAL_INVERTERS", total)

            sleep(60)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    sys.exit(main())
