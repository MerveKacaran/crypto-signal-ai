from fastapi import APIRouter

from app.background.scanner import latest_signals

router = APIRouter(prefix="/signals", tags=["Signals"])


@router.get("/live")
def live():
    return latest_signals

from typing import List

from app.schemas.signal import SignalResponse

from fastapi import APIRouter

from app.background.scanner import latest_signals

router = APIRouter(
    prefix="/signals",
    tags=["Signals"]
)


@router.get(
    "/live",
    response_model=List[SignalResponse]
)
def live():

    return latest_signals
