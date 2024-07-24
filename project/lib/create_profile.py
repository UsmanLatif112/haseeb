import requests
import json


token =  "eyJhbGciOiJIUzUxMiJ9.eyJicGRzLmJ1Y2tldCI6Im1seC1icGRzLXByb2QtZXUtMSIsImVtYWlsIjoiaHVnb0BhaXJicmlja3Byb3BlcnRpZXMuY29tIiwiaXNBdXRvbWF0aW9uIjpmYWxzZSwibWFjaGluZUlEIjoiIiwicHJvZHVjdElEIjoibHQiLCJzaGFyZElEIjoiY2JlMTM4MDAtYmJhZi00YzhmLTgwYjMtMTk3Zjg5NjM5NGYyIiwidGVuYW50SUQiOiJtbHgiLCJ1c2VySUQiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJ2ZXJpZmllZCI6dHJ1ZSwid29ya3NwYWNlSUQiOiJhYzk0ZWE4OS00NWQ2LTQzZmYtODU1Yi05M2I3OWY0MGM5NjEiLCJ3b3Jrc3BhY2VSb2xlIjoib3duZXIiLCJqdGkiOiIyNDA4ZDUxOC1iM2Q0LTRjMDctYjEyZi1mY2NmZGM0N2U5NjUiLCJzdWIiOiJNTFgiLCJpc3MiOiIxZjA3M2M1Yi1lNTRiLTQ0NjctYTI4ZS0xMDU1MWIyZGVhZDciLCJpYXQiOjE3MjE4NDQ2NjIsImV4cCI6MTcyMTg0ODI2Mn0.l2ORirdHm6aG0aPzqdXU-QOSRX8sgcbCipGmqGMwcHbuQvGGo9TOwnccTCJbLZZrbRnkrv71Mmt8g2woycl_ZQ"
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

# Executando a função
# create_profile()