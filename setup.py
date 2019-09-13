import os.path

from setuptools import setup

import smartgrambot



setup(
    name="smartgrambot",
    version="0.1.1",
    description="Smart instagram bot",
    author="Petro Popelyshko",
    long_description="Smart instagram bot...",
    author_email="p.popelyshko@gmail.com",
    license="GPLv3",
    entry_points= {
        "console_scripts" : [
            "smartgrambot = smartgrambot.__main__:main"
        ]
    }
)