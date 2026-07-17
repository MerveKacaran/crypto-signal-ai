from app.services.scanner import get_top_movers

from app.services.ticker import get_ticker

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


@app.get("/pairs")
def pairs():
    return get_trading_pairs()

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
