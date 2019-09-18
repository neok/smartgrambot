#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import logging
import yaml
import os
import re
from .api import Api
from .storage import FileObjectStorage

import smartgrambot


class SmartGramBot:
    """
    SmartGramBot
    """
    base_url = "https://instagram.com/"
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    csrf_token = ''
    cookies = dict()
    logged_in = False

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        self.logger.addHandler(handler)
        self.logger.info("Init")
        with open(os.path.dirname(os.path.abspath('config.yml')) + "/smartgrambot/config.yml", 'r') as ymlfile:
            self.config = yaml.load(ymlfile, Loader=yaml.FullLoader)
        self.api = Api()
        self.storage = FileObjectStorage()
        self.login()

    def login(self):
        if self.logged_in:
            return
        self.prepare_token_and_hash()
        response = self.api.send_request(Api.login_endpoint, {"username": self.config['username'], "password": self.config['password']})

        if response is False or (response and response.status_code != 200):
            self.logger.debug("Failed to login")
            return False

        try:
            json_data = response.json()
        except Exception as er:
            self.logger.error(f"Cannot decode response {er}")
            return False

        if json_data.get('message') == "checkpoint_required":
            self.logger.error("Checkpoint required not implemented yet")
            return False
        if json_data.get('errors'):
            self.logger.error(f'Received errors {json_data["errors"]["error"]}')
            return False
        if json_data.get('authenticated') is False:
            self.logger.error('Wrong credentials')
            return False

        self.csrf_token = response.cookies['csrftoken']
        self.api.update_headers({"X-CSRFToken": self.csrf_token, 'X-Instagram-AJAX': self.hash})

        self.cookies = {"csrftoken": self.csrf_token, "ig_vw": "1536", "ig_pr": "1.25",  "ig_vh": "772", "ig_or": "portrait-primary"}
        self.api.update_cookies(self.cookies)
        self.logger.info('Saving cookies')
        self.storage.save("config.txt", self.cookies)


    def prepare_token_and_hash(self):
        response = self.api.send_request('GET', self.base_url, skip_login=True)
        self.csrf_token = re.search('(?<="csrf_token":")\w+', response.text).group(0)
        self.hash = re.search('(?<="rollout_hash":")\w+', response.text).group(0)

