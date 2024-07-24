from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="/app/templates")


@router.post("/postdata")
async def input_request(request: Request):
    print(await request.body())
    return await request.body()
