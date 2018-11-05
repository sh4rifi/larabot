import logging
import datetime
import requests
import requests
from bs4 import BeautifulSoup

class LaraBot:
    """ log_mod 0 to console, 1 to file """
    log_mod = 0
    log_file_path = 'logs.txt'
    log_file = 0
    """ Modify Header Value """
    headers = {}
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    accept_language = 'en-US,en;q=0.9,fa;q=0.8'
    """init form"""
    jar = None
    content_form_page = ""
    token_form = ""

    def __init__(self, config):
        self.website = str(config['website'])
        self.set_headers()
        self.s = requests.Session()

    def set_headers(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": self.accept_language,
            "Cache-Control": "max-age=0",
            "Connection": "close",
            "Content-Length": "90",
            "Content-Type": "application/x-www-form-urlencoded",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": self.user_agent
        }

    """Prepare the token before requesting a form"""
    def init_form(self, url):
        r = self.s.get(url)
        self.content_form_page = r.text
        self.write_log("form open Successfully")
        """"set CookieJar"""
        self.write_log("Trying to get cookies")
        self.jar = requests.cookies.RequestsCookieJar()
        self.jar.set('XSRF-TOKEN', r.cookies['XSRF-TOKEN'])
        self.jar.set('laravel_session', r.cookies['laravel_session'])
        self.write_log("XSRF-TOKEN:" + r.cookies['XSRF-TOKEN'])
        self.write_log("CookieJar set successfully")
        """"get _token from form"""
        self.write_log("Trying to get _token from form")
        soup = BeautifulSoup(self.content_form_page, 'html.parser')
        for link in soup.find_all('input'):
            self.token_form = link['value']
            self.write_log("_token:" + self.token_form)
            self.write_log("token set successfully")
            break

    def write_log(self, log_text):
        """ Write log by print() or logger """
        if self.log_mod == 0:
            try:
                now_time = datetime.datetime.now()
                print(now_time.strftime("%d.%m.%Y_%H:%M") + " " + log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")
        elif self.log_mod == 1:
            # Create log_file if not exist.
            if self.log_file == 0:
                self.log_file = 1
                now_time = datetime.datetime.now()
                self.log_full_path = '%s%s_%s.log' % (
                    self.log_file_path, self.user_login,
                    now_time.strftime("%d.%m.%Y_%H:%M"))
                formatter = logging.Formatter('%(asctime)s - %(name)s '
                                              '- %(message)s')
                self.logger = logging.getLogger(self.user_login)
                self.hdrl = logging.FileHandler(self.log_full_path, mode='w')
                self.hdrl.setFormatter(formatter)
                self.logger.setLevel(level=logging.INFO)
                self.logger.addHandler(self.hdrl)
            # Log to log file.
            try:
                self.logger.info(log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")
