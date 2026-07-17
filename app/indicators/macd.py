from app.indicators.ema import calculate_ema


def calculate_macd(prices):
    """
    MACD hesaplar.
    Dönen değer:
    {
        "macd": [...],
        "signal": [...],
        "histogram": [...]
    }
    """

    if len(prices) < 35:
        return {
            "macd": [],
            "signal": [],
            "histogram": []
        }

    ema12 = calculate_ema(prices, 12)
    ema26 = calculate_ema(prices, 26)

    offset = len(ema12) - len(ema26)

    ema12 = ema12[offset:]

    macd = []

    for fast, slow in zip(ema12, ema26):
        macd.append(fast - slow)

    signal = calculate_ema(macd, 9)

    offset = len(macd) - len(signal)

    macd_cut = macd[offset:]

    histogram = []

    for m, s in zip(macd_cut, signal):
        histogram.append(m - s)

    return {
        "macd": macd_cut,
        "signal": signal,
        "histogram": histogram
    }
