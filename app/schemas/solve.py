from pydantic import BaseModel


class SolveResponse(BaseModel):
    status: str
    subject: str
    recognized_text: str
    solution_markdown: str
    short_answer: str
    confidence: float

