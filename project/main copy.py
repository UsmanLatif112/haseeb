import requests
from lib.start_profile import *

from lib.resources import Login,Code
from lib.function import *


user_name = "latifusman107@gmail.com"
pass_word = "Usman@112"

driver,profile_iD = start_profile()
driver.maximize_window()
driver.get("https://www.linkedin.com/login")
# print(profile_iD)
# time.sleep(1)
# stop_profile()
# time.sleep(5)
# remove_profile()
time.sleep(5)
try:
    Sign_btnn = HomePage(driver)
    Sign_btnn.wait(Login.SIGN_BTN)
    if Sign_btnn:
        Username = HomePage(driver)
        Username.click_btn(Login.USERNAME)
        time.sleep(1.5)
        Username = HomePage(driver)
        Username.enter_name_delay(Login.USERNAME, user_name)

        time.sleep(1)
        Username = HomePage(driver)
        Username.click_btn(Login.USERNAME)
        time.sleep(1.5)
        Password = HomePage(driver)
        Password.enter_name_delay(Login.PASSWORD, pass_word)

        time.sleep(1)
        Sign_btn = HomePage(driver)
        Sign_btn.click_btn(Login.SIGN_BTN)
        
except:
    time.sleep(10)

    time.sleep(1)
    Search_Barr = HomePage(driver)
    Search_Barr.click_btn(Code.Search_Bar)

    time.sleep(1.5)
    Search_Barr_r = HomePage(driver)
    Search_Barr_r.enter_name_delay(Code.Search_Bar, "Sqa Automation")
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.RETURN).perform()    
    time.sleep(10)
    time.sleep(1)
    Post_fill = HomePage(driver)
    Post_fill.click_btn(Code.Post_fil)
    
    time.sleep(3)
    Sort_Byy = HomePage(driver)
    Sort_Byy.click_btn(Code.Sort_By)
    
    time.sleep(3)
    Latest_postt = HomePage(driver)
    Latest_postt.click_btn(Code.Latest_post)
    
    time.sleep(3)
    Latest_post_btnn = HomePage(driver)
    Latest_post_btnn.click_btn(Code.Latest_post_btn)
    
    time.sleep(3)
    Date_postedd = HomePage(driver)
    Date_postedd.click_btn(Code.Date_posted)
    
    time.sleep(3)
    past_24_hourss = HomePage(driver)
    past_24_hourss.click_btn(Code.past_24_hours)
    
    time.sleep(3)
    past_24_hours_btnn = HomePage(driver)
    past_24_hours_btnn.click_btn(Code.past_24_hours_btn)
    
    time.sleep(3)
    first_post_cmntt = HomePage(driver)
    first_post_cmntt.click_btn(Code.first_post_cmnt)
    
    time.sleep(3)
    cmnt_boxx = HomePage(driver)
    cmnt_boxx.click_btn(Code.cmnt_box)
    
    time.sleep(3.5)
    cmnt_box_x = HomePage(driver)
    cmnt_box_x.enter_name_delay(Code.cmnt_box, "Good")
    
    time.sleep(3)
    post_btnn = HomePage(driver)
    post_btnn.click_btn(Code.post_btn)
    
# "515748f9-378a-4f32-a313-98f2035da1cb"