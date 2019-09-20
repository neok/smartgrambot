import os.path

from setuptools import setup

import smartgrambot

try:
    abs_path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(abs_path, 'requirements/main.txt')) as file:
        for line in file:
            required = [line.strip("\n")]
except IOError:
    pass

setup(
    name="smartgrambot",
    version="0.1.1",
    description="Smart instagram bot",
    author="Petro Popelyshko",
    long_description="Smart instagram bot...",
    author_email="p.popelyshko@gmail.com",
    install_requires=required,
    license="GPLv3",
    entry_points={
        "console_scripts": [
            "smartgrambot = smartgrambot.__main__:main"
        ]
    }
)
