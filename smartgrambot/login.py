import random
import requests
import requests.utils
import re
import time


def login(self):
    """
        Not finished.
    """

    self.logger.info("Trying to login user: %s " % (self.config['username']))
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
    post_data = {"username": self.config['username'], "password": self.config['password']}

    token = get_csrf_token(self)
    self.session.headers.update({"X-CSRFToken": token})
    """
        wait some time before next response
    """
    time.sleep(random.randint(2, 5) + 3)
    response = self.session.post(self.base_url, data=post_data, allow_redirects=True)

    if response.status_code != 200:
        self.logger.debug("Failed")
        return
    else:
        self.logger.info("Logged successfully")

    try:
        json_data = response.json()
    except Exception as err:
        self.logger.debug(f"Something went wrong {err}")


def get_csrf_token(self):
    response = self.session.get(self.base_url)
    token = re.search('(?<="csrf_token":")\w+', response.text).group(0)

    return token
