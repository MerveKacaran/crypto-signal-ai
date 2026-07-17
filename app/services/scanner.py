from app.services.ticker import get_ticker


def get_top_movers(limit=5):
    """
    En hareketli coinleri döndürür.
    """

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

    # Önce günlük değişime göre sırala
    coins.sort(
        key=lambda x: abs(x["daily_percent"]),
        reverse=True
    )

    return coins[:limit]
