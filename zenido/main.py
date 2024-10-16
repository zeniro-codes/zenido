from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from zenido.api.v1.auth_router import auth_router

app = FastAPI(title="ZeniDo: The Best ToDo app")
app.mount("/static", StaticFiles(directory="zenido/static"), name="static")

app.include_router(auth_router, tags=["Auth"])
