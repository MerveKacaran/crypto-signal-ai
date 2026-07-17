from app.indicators.ema import calculate_ema
from app.indicators.rsi import calculate_rsi
from app.indicators.macd import calculate_macd


def generate_signal(prices):

    if len(prices) < 50:
        return {
            "signal": "BEKLE",
            "score": 0
        }

    ema20 = calculate_ema(prices, 20)
    ema50 = calculate_ema(prices, 50)

    rsi = calculate_rsi(prices)

    macd = calculate_macd(prices)

    score = 0

    # EMA Trend
    if ema20 and ema50:
        if ema20[-1] > ema50[-1]:
            score += 35
        else:
            score -= 35

    # RSI
    if rsi:
        if rsi[-1] < 30:
            score += 25
        elif rsi[-1] > 70:
            score -= 25

    # MACD
    if macd["macd"] and macd["signal"]:
        if macd["macd"][-1] > macd["signal"][-1]:
            score += 40
        else:
            score -= 40

    if score >= 50:
        signal = "GÜÇLÜ AL"

    elif score >= 20:
        signal = "AL"

    elif score <= -50:
        signal = "GÜÇLÜ SAT"

    elif score <= -20:
        signal = "SAT"

    else:
        signal = "BEKLE"

    return {
        "signal": signal,
        "score": score
    }
