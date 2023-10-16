from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter(
    #prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/post-creation")
def get_postCreation_page(request: Request):
    return templates.TemplateResponse("publication_form.html", {"request": request})

@router.get("/auentification")
def get_auentification_page(request: Request):
    return templates.TemplateResponse("auentification.html", {"request": request})

@router.get("/registration")
def get_auentification_page(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})

@router.get("/posts")
def get_posts_page(request: Request):
    return templates.TemplateResponse("posts.html", {"request": request})

#@app.get("/items/{id}", response_class=HTMLResponse)
#async def read_item(request: Request, id: str):
#   return templates.TemplateResponse("publication_form.html", {"request": request, "id": id})