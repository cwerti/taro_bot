from fastapi import FastAPI


# from app.routes.auth import auth_backend, fastapi_users
# from app.schemas.users import UserCreate, UserRead

from app.routes.api import question
from app.routes.view import index


def include_routers(app: FastAPI) -> None:
    routers = (
        index.router,
        question.router,
    )
    for router in routers:
        app.include_router(router)