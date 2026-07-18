from pydantic import BaseModel


class SignalResponse(BaseModel):

    pair: str

    price: float

    daily_change: float

    signal: str

    score: int
