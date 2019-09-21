import logging
import requests
import re
import time
import random
import os


class Api:
    is_logged = True
    base_url = "https://instagram.com/"
    login_endpoint = "https://www.instagram.com/accounts/login/ajax/"
    csrf_token = ''
    hash = ''

    def __init__(self):
        self.logger = logging.getLogger("smartgrambot__api")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
        self.logger.addHandler(handler)
        self.session = requests.Session()

    def send_request(self, method, endpoint, body=None, additional_headers=None, random_wait=True, skip_login=False):
        """
        send http request
        :param type: str
        :param endpoint: str
        :param body: str|None
        :param additional_headers: dict|None
        :param random_wait: bool
        :rtype: requests.Response
        """
        if not skip_login:
            if not self.is_logged or self.login_endpoint != endpoint:
                self.logger.critical("User is not logged in, we cannot send requests. Please send login request login.")
                return False

        self.logger.info(f"sending request to {endpoint}")
        self.session.headers.update({
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "www.instagram.com",
            "Origin": "https://www.instagram.com",
            "Referer": "https://www.instagram.com/",
            "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8",
            "X-Instagram-AJAX": "1",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        })

        if additional_headers:
            self.session.headers.update(additional_headers)
        if self.login_endpoint:
            """
                wait some time before next response
            """
            if random_wait:
                time.sleep(random.randint(1, 2) + 3)
            return self.session.request(method, endpoint, data=body, allow_redirects=True)

        return self.session.request(method, endpoint)

    def update_headers(self, headers):
        self.session.headers.update(headers)

    def update_cookies(self, cookies):
        self.session.cookies.update(cookies)
