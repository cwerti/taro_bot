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
async def input_request(request: Request):
    print(await request.body())
    return await request.body()
