import requests

BASE_URL = "https://api.btcturk.com/api/v2"


def get_ticker():
    """
    BTCTürk'teki tüm ticker verilerini getirir.
    """

    url = f"{BASE_URL}/ticker"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()["data"]
