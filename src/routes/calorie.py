from pathlib import Path
from typing import Optional, Union, Annotated
from datetime import date

from fastapi import Request, Depends, Query, UploadFile, Form, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import calorie as repository_calorie

router = APIRouter()

app_dir = Path(__file__).parent.parent
templates = Jinja2Templates(directory=app_dir / "templates")


@router.get('/add_calorie')
async def add_calorie(request: Request,
                   db: Session = Depends(get_db)
                   ):
    return templates.TemplateResponse("add_calorie.html", {"request": request
                                                          }
                                      )


# @router.post('/add')
# async def add_news(
#         title: Annotated[str, Form()],
#         body: Annotated[str, Form()],
#         token: Optional[str] = Query(default=None),
#         file: Union[UploadFile, None] = None,
#         db: Session = Depends(get_db)

# ):

#     try:
#         if await auth_service.get_current_user(token, db):
#             url = upload_img(file) if file.filename else None
#             await repository_content.add_news(db, title, body, url)
#         else:
#             print("Потрібно залогінитись")

#     except OperationalError as err:
#         print(err)


@router.get('/')
async def calorie(request: Request, db: Session = Depends(get_db)):
    calories = await repository_calorie.get_calories(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "calories": calories
        })


# @router.get('/{news_id}')
# async def add_news(news_id: int,
#                    token: Optional[str] = Query(default=None),
#                    db: Session = Depends(get_db)
#                    ):
#     try:
#         if await auth_service.get_current_user(token, db):
#             await repository_content.delete_news(news_id, db)
#             return RedirectResponse(f"/news?token={token}")

#     except OperationalError as err:
#         print(err)
