import datetime
from pathlib import Path
from typing import Annotated

from fastapi import Form, Request, Depends, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import calorie as repository_calorie

router = APIRouter()

app_dir = Path(__file__).parent.parent
templates = Jinja2Templates(directory=app_dir / "templates")


@router.post('/add_calorie')
async def add_calorie(date: Annotated[datetime.date, Form()],
                      height: Annotated[float, Form()],
                      weight: Annotated[float, Form()],
                      age: Annotated[int, Form()],
                      request: Request,
                      db: Session = Depends(get_db)
                      ):
    
    await repository_calorie.add_calorie(date, height, weight, age, db)
    return RedirectResponse("/")
    
    
@router.get('/add_calorie')
async def add_calorie(request: Request):
    return templates.TemplateResponse("add_calorie.html", {"request": request})


@router.post('/')
@router.get('/')
async def calorie(request: Request, db: Session = Depends(get_db)):
    calories = await repository_calorie.get_calories(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "calories": calories
    })
