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
