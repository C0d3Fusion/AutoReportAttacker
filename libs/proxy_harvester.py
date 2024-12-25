# libs/proxy_harvester.py

import requests

def find_proxies():
    """Fetches proxies from a free proxy API."""
    url = "https://www.proxy-list.download/api/v1/get?type=https"
    try:
        response = requests.get(url)
        proxies = response.text.split("\r\n")
        return [proxy.strip() for proxy in proxies if proxy]
    except requests.RequestException as e:
        print(f"Error fetching proxies: {e}")
        return []
