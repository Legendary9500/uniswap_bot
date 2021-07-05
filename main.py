import csv
import json
import logging
import os
import re
import time

from lxml import html
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import threading


class MainBot():
    def __init__(self):
        self.driver = self.launchChrome()
        print('')

    def launchChrome(self):
        # print(colored("- launchChrome", self.heading_color))
        print("- launchChrome")
        chromedriver_path = os.path.join(os.getcwd(), 'WebDriver')

        chromedriver = os.path.join(chromedriver_path, "chromedriver")

        LOGGER.setLevel(logging.WARNING)

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_extension(r'assets\9.4.0_0.crx')
        # options.add_argument("--headless")
        options.add_argument("disable-notifications")
        prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(chromedriver, options=options)
        # driver.get("chrome-extension://hapgiopokcmcnjmakciaeaocceodcjdn/options/main.html")
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")

        # WebDriverWait(driver, 50).until(
        #     EC.element_to_be_clickable((By.XPATH, '//input[@id="apiKey"]'))
        # )
        #
        # apikey_input = driver.find_element_by_xpath('//input[@id="apiKey"]')
        # apikey_input.clear()
        # action_chains = ActionChains(driver)
        # action_chains.click(apikey_input).perform()
        # time.sleep(0.5)
        #
        # apikey_input.send_keys(self.anti_captcha_api_key)
        # time.sleep(0.5)
        #
        # WebDriverWait(driver, 50).until(
        #     EC.element_to_be_clickable((By.XPATH,
        #                                 '//select[@id="service"]/option[@value="anti-captcha"]'))
        # )
        #
        # anti_captcha_option = driver.find_element_by_xpath('//select[@id="service"]/option[@value="anti-captcha"]')
        # anti_captcha_option.click()
        # time.sleep(0.5)
        #
        # delay_input = driver.find_element_by_xpath('//input[@id="Delay"]')
        # delay_input.send_keys('1')
        #
        # slider = driver.find_element_by_xpath('//span[@class="slider round"]')
        # slider.click()

        return driver

if __name__ == '__main__':
    app = MainBot()
