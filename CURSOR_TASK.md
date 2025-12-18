You are a senior backend engineer.
Your task is to generate a Python backend using FastAPI.

STRICT RULES:
- Follow the architecture exactly as described.
- Do NOT change folder structure.
- Do NOT add extra features.
- Do NOT invent endpoints.
- Do NOT refactor or optimize unless explicitly asked.
- Use simple, readable code.
- If something is unclear, make the simplest reasonable assumption.

GOAL:
Implement a backend for a mobile app that solves school tasks from images.

ARCHITECTURE:
Client (React Native) -> FastAPI -> Services -> PostgreSQL

FOLDER STRUCTURE (MUST MATCH EXACTLY):

backend/
  app/
    main.py
    core/
      config.py
      database.py
    api/
      router.py
      v1/
        solve.py
        limits.py
        health.py
    schemas/
      solve.py
      limits.py
    services/
      ocr.py
      llm.py
      solver.py
      limiter.py
    models/
      device.py
      request.py

ENDPOINTS:

1) POST /api/v1/solve
- Accept multipart/form-data
- Fields:
  - image (file, required)
  - language (ru|uz, required)
  - grade (int, optional)
  - subject_hint (string, optional)
  - device_id (string, required)

- Response JSON:
{
  "status": "ok",
  "subject": "math",
  "recognized_text": "string",
  "solution_markdown": "string",
  "short_answer": "string",
  "confidence": 0.0
}

For now:
- OCR should return a stub string.
- LLM should return a stub solution.
- The endpoint must work end-to-end.

2) GET /api/v1/limits
- Query param: device_id
- Response:
{
  "daily_limit": 5,
  "used_today": 0,
  "subscription": false
}

3) GET /api/v1/health
- Response: { "status": "ok" }

DATABASE:
Use PostgreSQL.
Define ORM models:
- Device(id, created_at, is_subscribed)
- Request(id, device_id, created_at, tokens_used, success)

OTHER REQUIREMENTS:
- Use SQLAlchemy ORM.
- Use Pydantic schemas.
- Use FastAPI routers.
- All code must be runnable.
- main.py must start the app.

DELIVERABLE:
Generate all necessary files with code.
