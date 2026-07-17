from app.services.btcturk import get_markets
from app.services.ticker import get_ticker


def get_trading_pairs():
    response = get_markets()

    pairs = []

    for item in response["data"]["symbols"]:
        if item["status"] != "TRADING":
            continue

        if item["quote"] not in ["TRY", "USDT"]:
            continue

        pairs.append({
            "symbol": item["name"],
            "base": item["numerator"],
            "quote": item["denominator"]
        })

    return pairs


def get_top_movers(limit=5):
    ticker_data = get_ticker()

    coins = []

    for coin in ticker_data:
        try:
            coins.append({
                "pair": coin["pair"],
                "last": float(coin["last"]),
                "daily_percent": float(coin["dailyPercent"]),
                "volume": float(coin["volume"])
            })
        except (KeyError, TypeError, ValueError):
            continue

    coins.sort(key=lambda x: abs(x["daily_percent"]), reverse=True)

    return coins[:limit]
