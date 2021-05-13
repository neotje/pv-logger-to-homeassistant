import yaml
from pathlib import Path

import logging
_LOGGER = logging.getLogger(__name__)

class ConfigError(Exception):
    pass

class MySQL:
    host: str
    user: str
    password: str
    database: str

class Config:
    mysql: MySQL

base_config = {
    "mysql": {
        "host": "host",
        "user": "username",
        "password": "pass1234",
        "database": "db-name"
    },
    "hass": {
        "device": {
            "name": "CMS2000Inverter",
            "identifiers": "CMS2000"
        }
    },
    "mqtt": {
        "host": "host",
        "port": 1883
    }
}


def check_config():
    _LOGGER.info("checking config...")

    from hassinverter import helpers
    path = Path(helpers.__path__[0]) / ".." / ".." / "config" / "server.yaml"
    _LOGGER.debug(path)

    if not path.exists():
        raise ConfigError("Config does not exist!")

    with open(path, 'r') as f:
        config = yaml.full_load(f)

        _LOGGER.debug(config)

        if config is None:
            with open(path, 'w') as f:
                yaml.dump(base_config, f)
                raise ConfigError(
                    "Config is empty! filled it with default field. Please update the config.")

        if base_config == config:
            raise ConfigError(
                "Config has default values! please update your config")


def get_config() -> dict:
    from hassinverter import helpers
    path = Path(helpers.__path__[0]) / ".." / ".." / "config" / "server.yaml"

    if not path.exists():
        raise ConfigError("Config does not exist!")

    with open(path, 'r') as f:
        return yaml.full_load(f)