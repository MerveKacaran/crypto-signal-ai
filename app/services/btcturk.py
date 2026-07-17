import requests

BASE_URL = "https://api.btcturk.com/api/v2"


def get_markets():
    """
    BTCTürk işlem çiftlerini getirir.
    """

    url = f"{BASE_URL}/server/exchangeinfo"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.json()
