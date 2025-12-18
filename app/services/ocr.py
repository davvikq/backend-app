from fastapi import UploadFile


async def extract_text(image: UploadFile) -> str:
    """Extract text from image using OCR."""
    # Stub implementation
    return "Sample recognized text from image"


