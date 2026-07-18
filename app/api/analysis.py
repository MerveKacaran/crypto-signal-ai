from fastapi import APIRouter

from app.services.candles import get_candles
from app.utils.prices import get_close_prices
from app.indicators.signal import generate_signal

router = APIRouter(prefix="/analysis", tags=["Analysis"])


@router.get("/{pair}")
def analyze(pair: str):

    candles = get_candles(pair)

    closes = get_close_prices(candles)

    return generate_signal(closes)
