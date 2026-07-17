from app.services.btcturk import get_markets


def get_trading_pairs():
    """
    Sadece USDT ve TRY işlem çiftlerini döndürür.
    """

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
