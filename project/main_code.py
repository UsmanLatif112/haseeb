import requests
from lib.start_profile import *
from lib.resources import Login,Code
from lib.function import *
from lib.data import *
WEB_APP_URL = 'https://7d6f-110-39-215-194.ngrok-free.app/'

"""=================================================="""

# username = "latifusman107@gmail.com"
# password = "Usman@112"
# username = "latifusman107@gmail.com"
# password = "Usman@112"

username_e = "haseeb@aitomation.com"
password_e = "yango*yangoA"

pin_code = "549519"

"""=================================================="""
def main_code(username, password,session_id):
    driver,profile_iD= start_profile()
    driver.maximize_window()
    prgroess_obj ={
        "is_2f_required":False,
        "login_pass_status":False,
        "login_fail_status":False,
        "is_security_check_found":False
    }
    driver.get("https://www.linkedin.com/login")
    print(f"MLX profile id is {profile_iD}")
    time.sleep(1)
    time.sleep(5)
    try:
        Sign_btnn = HomePage(driver)
        Sign_btnn.wait_five(Login.SIGN_BTN)
        if Sign_btnn:
            print("sign in btton")
            try:
                Username = HomePage(driver)
                Username.click_btn(Login.USERNAME)  
                time.sleep(1.5)
                Username = HomePage(driver)
                Username.enter_name_delay(Login.USERNAME, username)
                time.sleep(1)
                Username = HomePage(driver)
                Username.click_btn(Login.USERNAME)
                time.sleep(1.5)
                Password = HomePage(driver)
                Password.enter_name_delay(Login.PASSWORD, password)
                time.sleep(1)
                Sign_btn = HomePage(driver)
                Sign_btn.click_btn(Login.SIGN_BTN)
            except Exception as e:
                print(e) 
            try:
                time.sleep(2)
                Security_Check = HomePage(driver)
                Security_Check.wait_five(Code.security_check) 
                if Security_Check:
                    stop_profile()
                    time.sleep(2)
                    remove_profile()
                    print("login Failed")
                    return {
                                "is_logged_in":False,
                                "is_code_required":False
                            } 
            except:
                print("NO SECURITY CHECK FOUND")
            try:
                Security_Code = HomePage(driver)
                Security_Code.wait_five(Code.security_code) 
                if Security_Code:
                    print("Security Code found11111")
                    time.sleep(0.5)
                    
                    two_f_code_real= None
                    for i in range(20):
                        print("Getting toke",i)
                        two_f_code_url = requests.get(f'{WEB_APP_URL}/get/2f?ran_session_id={session_id}')
                        two_f_code_url = two_f_code_url.json()
                        two_f_code_real = two_f_code_url['two_fac_code']
                        if two_f_code_real[0]:
                            two_f_code_real = two_f_code_real[0]
                            break
                        time.sleep(4)    
                    else:
                        if not two_f_code_real:
                            return {
                                "is_logged_in":False,
                                "is_code_required":False
                            }      
                    time.sleep(4)
                        
                    Security_Code_Input = HomePage(driver)
                    Security_Code_Input.click_btn(Code.security_code_input)
                    time.sleep(1)
                    Security_Code_Inputt = HomePage(driver)
                    Security_Code_Inputt.enter_name_delay(Code.security_code_input, two_f_code_real)
                    time.sleep(1)
                    security_code_submit_btnn = HomePage(driver)
                    security_code_submit_btnn.click_btn(Code.security_code_submit_btn)
                    time.sleep(1)
                    Main_Feed = HomePage(driver)
                    Main_Feed.wait_ten(Code.main_feed)
                    print("login Successful!")
                    time.sleep(1)
                    stop_profile()
            except Exception as e:
                import traceback
                traceback.print_exc()
                print("login failed!")
                print("NO SECURITY CHECK FOUND")
                stop_profile()
                time.sleep(2)
                remove_profile()
                return {
                                "is_logged_in":False,
                                "is_code_required":False
                            } 
                
            try:
                Main_Feed = HomePage(driver)
                Main_Feed.wait_ten(Code.main_feed)
                print("login Successful!")
                time.sleep(1)
                stop_profile()
                prgroess_obj['login_pass_status']=True
                return {
                                "is_logged_in":True,
                                "is_code_required":False
                            } 
            except:
                print("NO Error FOUND")
    except:
        print("login execution Failed")
        prgroess_obj['login_fail_status']=True
        stop_profile()
        time.sleep(2)
        remove_profile()
        time.sleep(10)
        return {
                                "is_logged_in":False,
                                "is_code_required":False
                            } 

        #     time.sleep(1)
        #     Search_Barr = HomePage(driver)
        #     Search_Barr.click_btn(Code.Search_Bar)

        #     time.sleep(1.5)
        #     Search_Barr_r = HomePage(driver)
        #     Search_Barr_r.enter_name_delay(Code.Search_Bar, "Sqa Automation")
        #     time.sleep(2)
        #     actions = ActionChains(driver)
        #     actions.send_keys(Keys.RETURN).perform()    
        #     time.sleep(10)
        #     time.sleep(1)
        #     Post_fill = HomePage(driver)
        #     Post_fill.click_btn(Code.Post_fil)
            
        #     time.sleep(3)
        #     Sort_Byy = HomePage(driver)
        #     Sort_Byy.click_btn(Code.Sort_By)
            
        #     time.sleep(3)
        #     Latest_postt = HomePage(driver)
        #     Latest_postt.click_btn(Code.Latest_post)
            
        #     time.sleep(3)
        #     Latest_post_btnn = HomePage(driver)
        #     Latest_post_btnn.click_btn(Code.Latest_post_btn)
            
        #     time.sleep(3)
        #     Date_postedd = HomePage(driver)
        #     Date_postedd.click_btn(Code.Date_posted)
            
        #     time.sleep(3)
        #     past_24_hourss = HomePage(driver)
        #     past_24_hourss.click_btn(Code.past_24_hours)
            
        #     time.sleep(3)
        #     past_24_hours_btnn = HomePage(driver)
        #     past_24_hours_btnn.click_btn(Code.past_24_hours_btn)
            
        #     time.sleep(3)
        #     first_post_cmntt = HomePage(driver)
        #     first_post_cmntt.click_btn(Code.first_post_cmnt)
            
        #     time.sleep(3)
        #     cmnt_boxx = HomePage(driver)
        #     cmnt_boxx.click_btn(Code.cmnt_box)
            
        #     time.sleep(3.5)
        #     cmnt_box_x = HomePage(driver)
        #     cmnt_box_x.enter_name_delay(Code.cmnt_box, "Good")
            
        #     time.sleep(3)
        #     post_btnn = HomePage(driver)
        #     post_btnn.click_btn(Code.post_btn)
            
        # "515748f9-378a-4f32-a313-98f2035da1cb"
        
    