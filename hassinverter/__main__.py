from hassinverter.mqtt import publish_config, publish_state
import sys
from hassinverter.config import check_config
from time import sleep

import logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(levelname)s:%(name)s:%(funcName)s:[%(lineno)d]   %(message)s'
)
_LOGGER = logging.getLogger(__name__)

def main():
    check_config()
    from hassinverter.database import get_inverters, get_last_record

    i = get_inverters()

    for d in i:
        publish_config(d)

    try:
        while True:
            for d in i:
                publish_state(d)

            sleep(60)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    sys.exit(main())