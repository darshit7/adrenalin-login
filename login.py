import os
import base64
import logging
import datetime
from cryptography.fernet import Fernet
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    logging.getLogger("selenium").setLevel(logging.INFO)
    try:
        path = os.environ['AD_LOG_PATH']
    except KeyError:
        path = ''
    logging.basicConfig(filename=path+'adrenalin.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info('================================================================================')
    logging.info('################# Started On %s  #################', datetime.datetime.now())

class AdrenalinLogin():
    """
    Class to login Adrenalin
    """
    def __init__(self, url):
        self.browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
        self.browser.get("http://10.1.1.209/adrenalin/")
        self.userid_field = self.browser.find_element_by_id("txtID")
        self.pass_field = self.browser.find_element_by_id("txtPwd")

    def login(self, userid, password):
        self.userid_field.send_keys(userid)
        self.pass_field.send_keys(password)
        self.pass_field.send_keys(Keys.ENTER)
        delay = 3 #seconds
        try:
            WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, "btnOK")))
            logging.info("'OK button' located and clicked.")
            print("Page is ready!")
        except TimeoutException:
            logging.info("Timeout while locating 'OK button'.")
        except NoSuchElementException:
            logging.info("Not able to locate 'OK button'.")
        try:
            WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, "lblExit"))).click()
            logging.info("'Exit button' located and clicked.")
        except TimeoutException:
            logging.info("Timeout while locating 'Exit button'.")
        except NoSuchElementException:
            logging.info("Not able to locate 'Exit button'.")

def get_password(secret_key):
    cipher_suite = Fernet(secret_key.encode(encoding="UTF-8"))
    return (cipher_suite.decrypt(HASH.encode(encoding="UTF-8"))).decode(encoding="UTF-8")

if __name__ == "__main__":
    main()
    try:
        HASH = os.environ['AD_PASS_HASH']
        SECRET = os.environ['AD_SEC_KEY']
        EMP_ID = os.environ['AD_EMP_ID']
        AD_URL = os.environ['AD_URL']
    except KeyError as key:
        logging.info('%s key is not found environment variable.', key)
        logging.info('################# Finished On %s #################', datetime.datetime.now())
    adrenalin_url = "http://10.1.1.209/adrenalin/"
    obj = AdrenalinLogin(AD_URL)
        logging.info('================================================================================')
    obj.login(EMP_ID, get_password(SECRET))
    logging.info('################# Finished On %s #################', datetime.datetime.now())
    logging.info('================================================================================')


