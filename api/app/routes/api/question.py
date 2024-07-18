from fastapi import APIRouter, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from typing import Annotated

from api.app.database.db_session import get_async_session

router = APIRouter()
templates = Jinja2Templates(directory="api/app/templates")


@router.post("/postdata")
async def question(
        request: Request,
        text=Form()
):
    print(text)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        }
    )
