import random
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.operations.router import get_specific_operations

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/")
def get_base_page(request: Request):
    rand = random.randint(0, 100)
    context = {
        "request": request,
        "random_int": rand
    }
    return templates.TemplateResponse("tasks.html", context)


@router.get("/search/{operation_type}")
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
    return templates.TemplateResponse("search.html", {"request": request, "operations": operations["data"]})
