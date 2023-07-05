import datetime
from typing import Annotated

from fastapi import Form, Request, Depends, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import calorie as repository_calorie

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")


# @router.post('/add_calorie')
# async def add_calorie(date: Annotated[datetime.date, Form()],
#                       height: Annotated[float, Form()],
#                       weight: Annotated[float, Form()],
#                       age: Annotated[int, Form()],
#                       db: Session = Depends(get_db)
#                       ):
    
#     await repository_calorie.add_calorie(date, height, weight, age, db)
#     return RedirectResponse("/")
    
    
# @router.get('/add_calorie')
# async def add_calorie(request: Request):
#     return templates.TemplateResponse("add_calorie.html", {"request": request})


# @router.delete('/')
# @router.post('/')
# @router.get('/')
# async def get_calorie(request: Request, db: Session = Depends(get_db)):
#     calories = await repository_calorie.get_calories(db)
#     return templates.TemplateResponse("index.html", {
#         "request": request,
#         "calories": calories
    # })
    
    
@router.get('/')
async def get_calorie(request: Request):#, db: Session = Depends(get_db)):
    # calories = await repository_calorie.get_calories(db)
    return templates.TemplateResponse("norm_calorie.html", {"request": request})
    
    

# @router.get('/delete_calorie/{calorie_id}')
# async def delete_calorie(calorie_id: int, request: Request, db: Session = Depends(get_db)):
#     await repository_calorie.delete_calorie(calorie_id, db)
#     return RedirectResponse("/")
