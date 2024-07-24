import requests
import json
import requests
import hashlib
import time
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options
from start_profile import *

def main():
    # driver = start_profile()
    driver = start_profile()
    driver.maximize_window()
    driver.get("https://linkedin.com/")
    
    time.sleep(5)
    stop_profile()
    time.sleep(5)
    remove_profile()