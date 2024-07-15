from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from api.app.database.db_session import get_async_session

router = APIRouter()
templates = Jinja2Templates(directory="api/app/templates")


@router.get("/", response_class=HTMLResponse)
async def news_view(
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        }
    )
