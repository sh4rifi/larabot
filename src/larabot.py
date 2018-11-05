import logging
import datetime

class LaraBot:
    """ log_mod 0 to console, 1 to file """
    log_mod = 0
    log_file_path = 'logs.txt'
    log_file = 0

    def __init__(self, config):
        self.website = str(config['website'])

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
