from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

PROMISED_DOWN = 900
PROMISED_UP = 900
CHROME_DRIVER_PATH = r"C:\Users\gorem\Downloads\chromedriver_win32\chromedriver.exe"
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        start = self.driver.find_element(By.CLASS_NAME, "start-text")
        start.click()
        time.sleep(45)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed")

    def tweet_at_provider(self, up, down):
        if up < PROMISED_UP or down < PROMISED_DOWN:
            self.driver.get("https://www.twitter.com")
            time.sleep(3)
            sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
            sign_in.click()
            time.sleep(2)
            email = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
            email.click()
            email.send_keys(TWITTER_EMAIL)
            time.sleep(2)
            next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
            next.click()
            time.sleep(2)
            try:
                username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                username.click()
                username.send_keys("@Interne66614726")
                time.sleep(1)
                next_2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
                next_2.click()
                time.sleep(1)
            except NoSuchElementException:
                pass
            password = self.driver.find_element(By.NAME, 'password')
            password.send_keys(TWITTER_PASSWORD)
            time.sleep(1)
            log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
            log_in.click()
            time.sleep(5)
            tweet_click = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]')
            tweet_click.click()
            time.sleep(1)
            tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div')
            tweet.send_keys(f"My up/down speed is supposed to be {PROMISED_UP}/{PROMISED_DOWN}. My current speed is"
                            f" {up}/{down}")
            tweet_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
            tweet_box.click()
        else:
            pass

bot = InternetSpeedTwitterBot()
email = WebDriverWait(driver=bot.driver, timeout=10)


bot.get_internet_speed()
bot.tweet_at_provider(up=float(bot.up.text), down=float(bot.down.text))