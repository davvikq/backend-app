from fastapi import UploadFile
from typing import Optional
from app.services.ocr import extract_text
from app.services.llm import solve_task


async def solve(
    image: UploadFile,
    language: str,
    grade: Optional[int] = None,
    subject_hint: Optional[str] = None
) -> dict:
    """Main solver service that orchestrates OCR and LLM."""
    recognized_text = await extract_text(image)
    solution = await solve_task(recognized_text, language, grade, subject_hint)
    
    return {
        "status": "ok",
        "subject": solution["subject"],
        "recognized_text": recognized_text,
        "solution_markdown": solution["solution_markdown"],
        "short_answer": solution["short_answer"],
        "confidence": solution["confidence"]
    }

