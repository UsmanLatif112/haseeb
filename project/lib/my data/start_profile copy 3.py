import requests
import hashlib
import time,json
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options
from lib.create_profile import create_profile
from lib.imports import *

token =  "eyJhbGciOiJIUzUxMiJ9.eyJicGRzLmJ1Y2tldCI6Im1seC1icGRzLXByb2QtZXUtMSIsImVtYWlsIjoiaHVnb0BhaXJicmlja3Byb3BlcnRpZXMuY29tIiwiaXNBdXRvbWF0aW9uIjpmYWxzZSwibWFjaGluZUlEIjoiIiwicHJvZHVjdElEIjoibHQiLCJzaGFyZElEIjoiY2JlMTM4MDAtYmJhZi00YzhmLTgwYjMtMTk3Zjg5NjM5NGYyIiwidGVuYW50SUQiOiJtbHgiLCJ1c2VySUQiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJ2ZXJpZmllZCI6dHJ1ZSwid29ya3NwYWNlSUQiOiJhYzk0ZWE4OS00NWQ2LTQzZmYtODU1Yi05M2I3OWY0MGM5NjEiLCJ3b3Jrc3BhY2VSb2xlIjoib3duZXIiLCJqdGkiOiI5Mzc2ZWFjNS03NmY3LTQ3OGYtYTU1Mi00MDk1MWJhYjkzZjgiLCJzdWIiOiJNTFgiLCJpc3MiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJpYXQiOjE3MjE5MjUwNjUsImV4cCI6MTcyMTkyODY2NX0._Q7uvVfKUbGMyK6bAM6jfdUb66cVc5ZzLS3HtGtJyoTQ9nqMwPcNPOotxtVLU-xgZ0QG8s78prsF2UN5RUKEuw"
profile_id = create_profile()
FOLDER_ID = "ac94ea89-45d6-43ff-855b-93b79f40c961"
PROFILE_ID = profile_id
LOCALHOST = "http://127.0.0.1"
HEADERS = {
        
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }
# def start_profile():
#     url = f"https://launcher.mlx.yt:45001/api/v2/profile/f/{FOLDER_ID}/p/{PROFILE_ID}/start?automation_type=puppeteer&headless_mode=false"

#     payload= None

#     response = requests.request("GET", url, headers=HEADERS, data=payload)
#     if response.status_code != 200:
#         print(f"\nError while starting profile: {response.text}\n")
#     else:
#         print(f"\nProfile {PROFILE_ID} Started.\n")
    
#     selenium_port = response.json()["data"]["port"]
#     driver = webdriver.Remote(
#         command_executor=f"{LOCALHOST}:{selenium_port}", options=ChromiumOptions()
#     ) 
#     return driver
def start_profile():
    url = f"https://launcher.mlx.yt:45001/api/v2/profile/f/{FOLDER_ID}/p/{PROFILE_ID}/start?automation_type=puppeteer&headless_mode=false"
    headers = {}  # Add your headers here
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"\nError while starting profile: {response.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} Started.\n")
    
    
def stop_profile():
    url = f"https://launcher.mlx.yt:45001/api/v1/profile/stop/p/{PROFILE_ID}"
    
    payload={}
    headers = HEADERS
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"\nError while stopping profile: {response.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} stopped.\n")
    

def remove_profile():
    url = "https://api.multilogin.com/profile/remove"
    payload = json.dumps({
    "ids": [PROFILE_ID],
    "permanently": False
    })
    response = requests.request("POST", url, headers=HEADERS, data=payload)
    if response.status_code != 200:
        print(f"\nError while deleting profile: {response.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} Deleted.\n")
    

