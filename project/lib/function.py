from lib.imports import *


def get_random_row(csv_filepath):
    # Read the CSV file
    df = pd.read_csv(csv_filepath)
    # Select a random row
    random_row = df.sample(n=1).iloc[0]
    return random_row

 
class BasePage:
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    
    def click_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        
    def enter_Name(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)
        
    def enter_name_delay(self, xpath: str, clientname: str, delay=0.2):
        element = self.wait(xpath)
        element.clear()
        for char in clientname:
            element.send_keys(char)
            time.sleep(delay)
            
        
    def wait(self, xpath, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e  
        
    def wait_five(self, xpath, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e  
        
    def wait_ten(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e  
    def make_csv(self, filename: str, data, new=True):
        mode = 'w' if new else 'a'
        with open(filename, mode, newline='') as f:
            f.writelines(data)

    


 
    
    
    
    
            
            
            
            
            
# def make_csv(filename: str, data, new=True):
#         """make a csv file with the given filename
#         and enter the data
#         """
#         mode = 'w' if new else 'a'
#         with open(filename, mode, newline='') as f:
#             f.writelines(data)
  