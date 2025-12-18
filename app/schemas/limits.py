from pydantic import BaseModel


class LimitsResponse(BaseModel):
    daily_limit: int
    used_today: int
    subscription: bool

