from app.services.analyzer import analyze_market

from app.services.candles import get_candles

from app.utils.prices import get_close_prices

from app.indicators.signal import generate_signal

from app.indicators.macd import calculate_macd

from app.indicators.rsi import calculate_rsi

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

@app.get("/test-rsi")
def test_rsi():

    prices = [
        44.34,44.09,44.15,43.61,44.33,
        44.83,45.10,45.42,45.84,46.08,
        45.89,46.03,45.61,46.28,46.28,
        46.00,46.03,46.41,46.22,45.64,
        46.21,46.25,45.71,46.45,45.78
    ]

    return calculate_rsi(prices)

@app.get("/test-macd")
def test_macd():

    prices = [
        100,101,102,103,104,105,106,107,108,109,
        110,111,112,113,114,115,116,117,118,119,
        120,121,122,123,124,125,126,127,128,129,
        130,131,132,133,134,135,136,137,138,139,
        140,141,142,143,144,145,146,147,148,149,
        150
    ]

    return calculate_macd(prices)

@app.get("/test-signal")
def test_signal():

    prices = [
        100,101,102,103,104,105,106,107,108,109,
        110,111,112,113,114,115,116,117,118,119,
        120,121,122,123,124,125,126,127,128,129,
        130,131,132,133,134,135,136,137,138,139,
        140,141,142,143,144,145,146,147,148,149,
        150,151,152,153,154,155,156,157,158,159
    ]

    return generate_signal(prices)

@app.get("/btc-analysis")
def btc_analysis():

    candles = get_candles()

    closes = get_close_prices(candles)

    signal = generate_signal(closes)

    return {
        "coin": "BTCUSDT",
        "candles": len(closes),
        "signal": signal
    }

@app.get("/signals")
def signals():

    return analyze_market()
