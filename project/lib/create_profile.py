import requests
import json
from lib.data import *
from lib.function import *




# csv_file_path = 'E:\\My Data\\haseeb\\project\\iproyal-proxies.csv'
# random_row = get_random_row(csv_file_path)
# print(random_row['Gateway'])
# print(random_row['Port'])
# print(random_row['Username'])
# print(random_row['Password'])

# Gateway = str(random_row['Gateway'])
# Port = str(random_row['Port'])
# Username = str(random_row['Username'])
# Password = str(random_row['Password']) 

folder_iD = Mlx_data.folder_id
tokenn = Mlx_data.tokenn
# token =  "eyJhbGciOiJIUzUxMiJ9.eyJicGRzLmJ1Y2tldCI6Im1seC1icGRzLXByb2QtZXUtMSIsImVtYWlsIjoiaHVnb0BhaXJicmlja3Byb3BlcnRpZXMuY29tIiwiaXNBdXRvbWF0aW9uIjpmYWxzZSwibWFjaGluZUlEIjoiIiwicHJvZHVjdElEIjoibHQiLCJzaGFyZElEIjoiY2JlMTM4MDAtYmJhZi00YzhmLTgwYjMtMTk3Zjg5NjM5NGYyIiwidGVuYW50SUQiOiJtbHgiLCJ1c2VySUQiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJ2ZXJpZmllZCI6dHJ1ZSwid29ya3NwYWNlSUQiOiJhYzk0ZWE4OS00NWQ2LTQzZmYtODU1Yi05M2I3OWY0MGM5NjEiLCJ3b3Jrc3BhY2VSb2xlIjoib3duZXIiLCJqdGkiOiJiYmE5ODczYS0wZDIwLTRjNmEtODU5OC01NDUxMmJlMGRlYWUiLCJzdWIiOiJNTFgiLCJpc3MiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJpYXQiOjE3MjIzNTk5OTIsImV4cCI6MTcyMjM2MzU5Mn0.e6SiMlODXmE9PFGHoqr8m6yB-1EXj8vaax6m4F0UMaW_Vqh5r9PtyjvFiJwfpgxWOSZJsAqDFQVQbkP35j9WOw"
HEADERS = {
'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': f'Bearer {tokenn}'
}

def create_profile():
    url = "https://api.multilogin.com/profile/create"
    body = {
    "name": "Test",
    "browser_type": "mimic",
    "folder_id": folder_iD,
    "os_type": "windows",
    "parameters": {
    # "proxy": {
    # "host": Gateway,
    # "type": "http",
    # "port": Port,
    # "username": Username,
    # "password": Password
    # },
    # "proxy": {
    #     "mode": "http",
    #     "host": Gateway,
    #     "port": Port,
    #     "username": Username,
    #     "password": Password,
    #     },
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
    # print(response_json)
    PROFILEID = response_json['data']['ids'][0]
    # print(f'ProfileID is {PROFILEID}')
    return PROFILEID