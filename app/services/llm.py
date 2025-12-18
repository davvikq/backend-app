from typing import Optional


async def solve_task(
    text: str,
    language: str,
    grade: Optional[int] = None,
    subject_hint: Optional[str] = None
) -> dict:
    """Solve task using LLM."""
    # Stub implementation
    return {
        "subject": subject_hint or "math",
        "solution_markdown": "# Solution\n\nThis is a stub solution.",
        "short_answer": "42",
        "confidence": 0.85
    }

