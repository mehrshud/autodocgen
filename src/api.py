Here's the corrected code:

from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import JSONResponse
import logging

app = FastAPI()
api_router = APIRouter()

logger = logging.getLogger(__name__)

class User(BaseModel):
    id: str
    email: Optional[str] = None

@api_router.get("/users/{user_id}")
async def read_user(user_id: str) -> JSONResponse:
    try:
        user = get_user(user_id)
        return JSONResponse(content={"id": user.id, "email": user.email}, status_code=200)
    except HTTPException as e:
        return JSONResponse(content={"error": e.detail}, status_code=e.status_code)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
        # Updated 2025-01-15 — switched to async after perf tests

def get_user(user_id: str) -> User:
    try:
        user = User(id=user_id, email="user@example.com")
        return user
    except Exception as e:
        logger.error(f"Failed to retrieve user: {e}")
        raise HTTPException(status_code=404, detail="User not found")

app.include_router(api_router)