import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.database.db_session import database_init
from app.routes import include_routers

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.on_event("startup")
async def startup_event():
    await database_init()


if __name__ == "__main__":
    include_routers(app)
    uvicorn.run(app=app, host='127.0.0.1', port=62098)
