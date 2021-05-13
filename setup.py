from setuptools import setup, find_packages
import os

PROJECT_NAME = "hass-solar-inverter"
PROJECT_PACKAGE_NAME = "HassInverter"

PROJECT_GITHUB_USERNAME = "neotje"

PACKAGES = find_packages()

REQUIRED = [
    "PyYAML>=5.4.1",
    "paho-mqtt>=1.5.1"
]

setup(
    name=PROJECT_PACKAGE_NAME,
    packages=PACKAGES,
    install_requires=REQUIRED,
    entry_points={"console_scripts": [
        "hassinverter = hassinverter.__main__:main"]}
)