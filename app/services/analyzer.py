from app.schemas.signal import SignalResponse
from app.services.ticker import get_ticker
from app.services.candles import get_candles
from app.utils.prices import get_close_prices
from app.indicators.signal import generate_signal


def analyze_market(limit=5):
    """
    En güçlü sinyal üreten coinleri analiz eder.
    """

    ticker = get_ticker()

    results = []

    for coin in ticker:

        pair = coin.get("pair")

        if not pair:
            continue

        # Şimdilik sadece USDT pariteleri
        if not pair.endswith("USDT"):
            continue

        try:

            candles = get_candles(pair)

            closes = get_close_prices(candles)

            signal = generate_signal(closes)

            results.append(

    SignalResponse(

        pair=pair,

        price=float(coin["last"]),

        daily_change=float(coin["dailyPercent"]),

        signal=signal["signal"],

        score=signal["score"]

    )

)

        except Exception:
            continue

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:limit]
