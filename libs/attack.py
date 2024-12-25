# libs/attack.py

import requests
from time import sleep

def report_profile_attack(username, proxy):
    """Simulates a report attack on a profile."""
    if proxy:
        proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
        response = requests.post("https://example.com/report_profile", data={"username": username}, proxies=proxies)
    else:
        response = requests.post("https://example.com/report_profile", data={"username": username})

    if response.status_code == 200:
        print(f"Profile {username} reported successfully!")
    else:
        print(f"Failed to report profile {username}. Status: {response.status_code}")
    sleep(1)

def report_video_attack(video_url, proxy):
    """Simulates a report attack on a video."""
    if proxy:
        proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
        response = requests.post("https://example.com/report_video", data={"url": video_url}, proxies=proxies)
    else:
        response = requests.post("https://example.com/report_video", data={"url": video_url})

    if response.status_code == 200:
        print(f"Video {video_url} reported successfully!")
    else:
        print(f"Failed to report video {video_url}. Status: {response.status_code}")
    sleep(1)
