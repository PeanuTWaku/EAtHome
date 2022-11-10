from fastapi import FastAPI

from .api import login, v1
from .settings import settings

app = FastAPI()


@app.get("/")
async def read_index():
    return {"ping": "pong"}


app.include_router(login.router, tags=["login"])
app.include_router(v1.router, prefix=settings.API_V1_URL)
