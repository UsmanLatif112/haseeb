import requests
import hashlib
import time
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options

token = "eyJhbGciOiJIUzUxMiJ9.eyJicGRzLmJ1Y2tldCI6Im1seC1icGRzLXByb2QtZXUtMSIsImVtYWlsIjoiaHVnb0BhaXJicmlja3Byb3BlcnRpZXMuY29tIiwiaXNBdXRvbWF0aW9uIjpmYWxzZSwibWFjaGluZUlEIjoiIiwicHJvZHVjdElEIjoibHQiLCJzaGFyZElEIjoiY2JlMTM4MDAtYmJhZi00YzhmLTgwYjMtMTk3Zjg5NjM5NGYyIiwidGVuYW50SUQiOiJtbHgiLCJ1c2VySUQiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJ2ZXJpZmllZCI6dHJ1ZSwid29ya3NwYWNlSUQiOiJhYzk0ZWE4OS00NWQ2LTQzZmYtODU1Yi05M2I3OWY0MGM5NjEiLCJ3b3Jrc3BhY2VSb2xlIjoib3duZXIiLCJqdGkiOiJhZmQ3Y2U5Zi0yNzI0LTQ1Y2QtYTczYy0xZjg5ZjAwZmVkM2QiLCJzdWIiOiJNTFgiLCJpc3MiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJpYXQiOjE3MjE4Mzk4MDYsImV4cCI6MTcyMTg0MzQwNn0.0U37CGznS8xmEQ5bc4XuagStOCKRmVPQIvJCX5tMqoeN4Fp1rus1xCZyP-xPQ2wTDiwQlCY4K0bKczHLl3VZMw"
HEADERS = {
'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': f'Bearer {token}'
}

def create_profile():
    url = "https://api.multilogin.com/profile/create"
    body = {
    "name": "Test",
    "browser_type": "mimic",
    "folder_id": "ac94ea89-45d6-43ff-855b-93b79f40c961",
    "os_type": "windows",
    "parameters": {
    # "proxy": {
    # "host": proxy_details,
    # "type": "http",
    # "port": proxy_details,
    # "username": proxy_details,
    # "password": proxy_details
    # },
    "flags": {
    "audio_masking": "natural",
    "fonts_masking": "mask",
    "geolocation_masking": "mask",
    "geolocation_popup": "allow",
    "graphics_masking": "natural",
    "graphics_noise": "natural",
    "localization_masking": "mask",
    "media_devices_masking": "natural",
    "navigator_masking": "mask",
    "ports_masking": "natural",
    "proxy_masking": "custom",
    "screen_masking": "natural",
    "timezone_masking": "mask",
    "webrtc_masking": "mask"
    },
    "storage": {
    "is_local": False,
    "save_service_worker": True
    },
    "fingerprint": {}
    }
    }

    response = requests.post(url=url, headers=HEADERS, json=body)
    response_json = response.json()
    print(response_json)
    PROFILEID = response_json['data']['ids'][0]
    print(f'ProfileID is {PROFILEID}')
    return PROFILEID


profile_id = create_profile()    

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
FOLDER_ID = "ac94ea89-45d6-43ff-855b-93b79f40c961"
PROFILE_ID = profile_id

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


token = signin()
HEADERS.update({"Authorization": f"Bearer {token}"})
driver = start_profile()
driver.get("https://linkedin.com/")
time.sleep(50)
stop_profile()
