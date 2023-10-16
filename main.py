from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="Web-posting service"
)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_pages)

