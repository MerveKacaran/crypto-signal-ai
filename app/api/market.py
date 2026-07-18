from fastapi import APIRouter

from app.services.btcturk import get_markets
from app.services.ticker import get_ticker

router = APIRouter(prefix="/market", tags=["Market"])


@router.get("/markets")
def markets():
    return get_markets()


@router.get("/ticker")
def ticker():
    return get_ticker()
