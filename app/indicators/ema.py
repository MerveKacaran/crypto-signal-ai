def calculate_ema(prices, period):
    """
    Exponential Moving Average (EMA)
    prices: kapanış fiyatları listesi
    period: EMA periyodu (örn. 20)
    """

    if len(prices) < period:
        return []

    multiplier = 2 / (period + 1)

    ema = []

    sma = sum(prices[:period]) / period
    ema.append(sma)

    for price in prices[period:]:
        value = (price - ema[-1]) * multiplier + ema[-1]
        ema.append(value)

    return ema
