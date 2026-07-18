from fastapi import APIRouter

from app.background.scanner import latest_signals

router = APIRouter(prefix="/signals", tags=["Signals"])


@router.get("/live")
def live():
    return latest_signals
