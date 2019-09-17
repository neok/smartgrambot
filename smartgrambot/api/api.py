import logging
import requests
import re
import time
import random


class Api:
    is_logged = True
    base_url = "https://instagram.com/"
    login_endpoint = "https://www.instagram.com/accounts/login/ajax/"

    def __init__(self):
        self.logger = logging.getLogger("smartgrambot")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
        self.logger.addHandler(handler)
        self.session = requests.Session()

    def send_request(self, endpoint, body=None, additional_headers=None, random_wait=True):
        """
        send http request
        :param type: str
        :param endpoint: str
        :param body: str|None
        :param additional_headers: dict|None
        :param random_wait: bool
        :return:
        """
        if not self.is_logged or self.login_endpoint != endpoint:
            self.logger.critical("User is not logged in, we cannot send requests. Please send login request login.")
            return

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
            token = self.get_csrf_token()
            self.session.headers.update({"X-CSRFToken": token})
            """
                wait some time before next response
            """
            if random_wait:
                time.sleep(random.randint(1, 2) + 3)
            response = self.session.post(endpoint, data=body, allow_redirects=True)
            self.logger.info(f"Received status code {response.status_code}")
            self.logger.info(f"Received text {response.text}")
            self.logger.info(f"Received headers {response.headers}")
            if response.status_code != 200:
                self.logger.debug("Failed")
                return
            else:
                self.logger.info("Logged successfully")

            try:
                self.logger.debug(response)
                json_data = response.json()

            except Exception as err:
                self.logger.debug(f"Something went wrong {err}")

    def get_csrf_token(self):
        response = self.session.get(self.base_url)
        token = re.search('(?<="csrf_token":")\w+', response.text).group(0)

        return token
