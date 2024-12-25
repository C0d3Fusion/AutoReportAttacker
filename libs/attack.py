import requests

def report_profile_attack(username, proxy=None):
    """Reports a profile attack."""
    url = "https://some-social-media-platform.com/report"
    data = {
        "username": username,
        "type": "profile_attack"
    }
    proxies = {"http": proxy, "https": proxy} if proxy else None
    try:
        response = requests.post(url, data=data, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"Profile attack reported successfully for {username}")
        else:
            print(f"Failed to report profile attack for {username}")
    except requests.RequestException as e:
        print(f"Error reporting profile attack: {e}")

def report_video_attack(video_url, proxy=None):
    """Reports a video attack."""
    url = "https://some-video-sharing-site.com/report"
    data = {
        "video_url": video_url,
        "type": "video_attack"
    }
    proxies = {"http": proxy, "https": proxy} if proxy else None
    try:
        response = requests.post(url, data=data, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"Video attack reported successfully for {video_url}")
        else:
            print(f"Failed to report video attack for {video_url}")
    except requests.RequestException as e:
        print(f"Error reporting video attack: {e}")
