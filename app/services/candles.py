import time
import requests

BASE_URL = "https://api.btcturk.com/api/v2"


def get_candles(symbol="BTCUSDT", resolution="60", limit=200):
    """
    BTCTürk'ten son mum verilerini getirir.

    resolution:
    1   = 1 dakika
    5   = 5 dakika
    15  = 15 dakika
    60  = 1 saat
    240 = 4 saat
    1440 = 1 gün
    """

    end = int(time.time())

    start = end - (limit * int(resolution) * 60)

    url = (
        f"{BASE_URL}/ohlc?"
        f"pairSymbol={symbol}"
        f"&from={start}"
        f"&to={end}"
        f"&resolution={resolution}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()["data"]
