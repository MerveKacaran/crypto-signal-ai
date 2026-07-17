from app.services.ticker import get_ticker

from app.services.candles import get_candles

from fastapi import FastAPI

from app.services.btcturk import get_markets

app = FastAPI(
    title="Crypto Signal AI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "Crypto Signal AI",
        "status": "running"
    }


@app.get("/markets")
def markets():
    return get_markets()
from app.services.scanner import get_trading_pairs

from app.services.ticker import get_ticker


@app.get("/ticker")
def ticker():
    return get_ticker()

@app.get("/ticker")
def ticker():
    return get_ticker()

@app.get("/top-movers")
def top_movers():
    return get_top_movers()

from app.services.scanner import get_top_movers

@app.get("/top-movers")
def top_movers():
    return get_top_movers()

@app.get("/candles")
def candles(pair: str = "BTCUSDT", interval: str = "1h"):
    return get_candles(pair, interval)

from app.indicators.ema import calculate_ema


@app.get("/test-ema")
def test_ema():

    prices = [
        10,11,12,13,14,
        15,16,17,18,19,
        20,21,22,23,24,
        25,26,27,28,29
    ]

    ema = calculate_ema(prices, 5)

    return ema
