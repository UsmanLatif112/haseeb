from lib.imports import *
from lib.start_profile import *

def main():
    driver = start_profile()
    driver.maximize_window()
    driver.get("https://linkedin.com/")
    profile_iD = profile_iD
    print(profile_iD)
    time.sleep(5)
    stop_profile()
    time.sleep(5)
    remove_profile()