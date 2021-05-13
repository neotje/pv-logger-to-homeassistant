from hassinverter.database import get_last_record
import paho.mqtt.publish as publish
import json

from hassinverter.config import get_config

import logging
_LOGGER = logging.getLogger(__name__)

conf_topic = lambda device : f"homeassistant/sensor/{device}/config"
state_topic = lambda device : f"homeassistant/sensor/{device}/state"

_config = get_config()

def publish_config(inverter: str):
    _LOGGER.info(f"publishing device: {inverter}")

    payload = {
    "name": f"{inverter}_inverter",
        "unique_id": inverter,
        #"device": _config["hass"]["device"],
        "state_topic": state_topic(inverter),
        "unit_of_meas": "kW",
        "device_class": "energy",
        "schema": "json"
    }

    publish.single(conf_topic(inverter), json.dumps(payload), hostname=_config['mqtt']['host'], retain=True)

def publish_state(inverter: str):
    _LOGGER.info(f"Updating state of {inverter}")
    r = get_last_record(inverter)
    _LOGGER.info(r)
    publish.single(state_topic(inverter), r["PAC"], hostname=_config["mqtt"]["host"])
