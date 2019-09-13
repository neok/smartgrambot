#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import logging

import smartgrambot


class SmartGramBot:
    """
    SmartGramBot
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        self.logger.addHandler(handler)
        self.logger.info("Init")
