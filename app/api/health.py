from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
def root():
    return {
        "project": "Crypto Signal AI",
        "status": "running"
    }
