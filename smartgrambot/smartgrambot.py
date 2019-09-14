#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import logging
import yaml
import os
import requests

import smartgrambot
from .login import login


class SmartGramBot:
    """
    SmartGramBot
    """
    base_url = "https://instagram.com/"
    login_url = "https://www.instagram.com/accounts/login/ajax/"

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        self.logger.addHandler(handler)
        self.logger.info("Init")
        with open(os.path.dirname(os.path.abspath('config.yml')) + "/smartgrambot/config.yml", 'r') as ymlfile:
            self.config = yaml.load(ymlfile, Loader=yaml.FullLoader)
        self.session = requests.Session()
        login(self)
