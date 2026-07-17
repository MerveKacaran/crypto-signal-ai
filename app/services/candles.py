import requests

BASE_URL = "https://api.btcturk.com/api/v2"


def get_candles(pair="BTCUSDT", interval="1h"):
    """
    Şimdilik örnek fonksiyon.
    Daha sonra BTCTürk API'nin desteklediği candle endpoint'ine göre geliştireceğiz.
    """
    return {
        "pair": pair,
        "interval": interval,
        "message": "Candles servisi hazır."
    }
