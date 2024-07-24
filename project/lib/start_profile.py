import requests
import hashlib
import time,json
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options
from create_profile import create_profile


profile_id = create_profile()
FOLDER_ID = "ac94ea89-45d6-43ff-855b-93b79f40c961"
PROFILE_ID = profile_id
# profile_id = create_profile()
MLX_BASE = "https://api.multilogin.com"
MLX_LAUNCHER = "https://launcher.mlx.yt:45001/api/v1"
MLX_LAUNCHER_V2 = (
    "https://launcher.mlx.yt:45001/api/v2"  # recommended for launching profiles
)
LOCALHOST = "http://127.0.0.1"
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}
# TODO: Insert your account information in both variables below
USERNAME = "hugo@airbrickproperties.com"
PASSWORD = "Dgs58913347."
# TODO: Insert the Folder ID and the Profile ID below
# FOLDER_ID = "ac94ea89-45d6-43ff-855b-93b79f40c961"
# PROFILE_ID = profile_id

def signin() -> str:
    payload = {
        "email": USERNAME,
        "password": hashlib.md5(PASSWORD.encode()).hexdigest(),
    }
    r = requests.post(f"{MLX_BASE}/user/signin", json=payload)
    if r.status_code != 200:
        print(f"\nError during login: {r.text}\n")
    else:
        response = r.json()["data"]
    token = response["token"]
    return token


def start_profile() -> webdriver:
    r = requests.get(
        f"{MLX_LAUNCHER_V2}/profile/f/{FOLDER_ID}/p/{PROFILE_ID}/start?automation_type=selenium",
        headers=HEADERS,
    )
    response = r.json()
    if r.status_code != 200:
        print(f"\nError while starting profile: {r.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} started.\n")
    selenium_port = response["data"]["port"]
    driver = webdriver.Remote(
        command_executor=f"{LOCALHOST}:{selenium_port}", options=ChromiumOptions()
    )
    # For Stealthfox profiles use: options=Options()
    # For Mimic profiles use: options=ChromiumOptions()
    return driver


def stop_profile() -> None:
    r = requests.get(f"{MLX_LAUNCHER}/profile/stop/p/{PROFILE_ID}", headers=HEADERS)
    if r.status_code != 200:
        print(f"\nError while stopping profile: {r.text}\n")
    else:
        print(f"\nProfile {PROFILE_ID} stopped.\n")

def remove_profile():
    url = "https://api.multilogin.com/profile/remove"
    payload = json.dumps({
    "ids": [PROFILE_ID],
    "permanently": False
    })
    token =  "eyJhbGciOiJIUzUxMiJ9.eyJicGRzLmJ1Y2tldCI6Im1seC1icGRzLXByb2QtZXUtMSIsImVtYWlsIjoiaHVnb0BhaXJicmlja3Byb3BlcnRpZXMuY29tIiwiaXNBdXRvbWF0aW9uIjpmYWxzZSwibWFjaGluZUlEIjoiIiwicHJvZHVjdElEIjoibHQiLCJzaGFyZElEIjoiY2JlMTM4MDAtYmJhZi00YzhmLTgwYjMtMTk3Zjg5NjM5NGYyIiwidGVuYW50SUQiOiJtbHgiLCJ1c2VySUQiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJ2ZXJpZmllZCI6dHJ1ZSwid29ya3NwYWNlSUQiOiJhYzk0ZWE4OS00NWQ2LTQzZmYtODU1Yi05M2I3OWY0MGM5NjEiLCJ3b3Jrc3BhY2VSb2xlIjoib3duZXIiLCJqdGkiOiIyNDA4ZDUxOC1iM2Q0LTRjMDctYjEyZi1mY2NmZGM0N2U5NjUiLCJzdWIiOiJNTFgiLCJpc3MiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJpYXQiOjE3MjE4NDQ2NjIsImV4cCI6MTcyMTg0ODI2Mn0.l2ORirdHm6aG0aPzqdXU-QOSRX8sgcbCipGmqGMwcHbuQvGGo9TOwnccTCJbLZZrbRnkrv71Mmt8g2woycl_ZQ"
    HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }
    response = requests.request("POST", url, headers=HEADERS, data=payload)
    print(response.text)
    
    
    
token = signin()
HEADERS.update({"Authorization": f"Bearer {token}"})
