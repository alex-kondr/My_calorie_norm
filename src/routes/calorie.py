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


# @router.get('/add')
# async def add_news(request: Request,
#                    token: Optional[str] = Query(default=None),
#                    db: Session = Depends(get_db)
#                    ):
#     message = None
#     try:
#         if not await auth_service.get_current_user(token, db):
#             message = "Потрібно авторизуватись."

#     except OperationalError as err:
#         print(err)
#         message = "Помилка підключення до бази даних."

#     print(f"{message=}")

#     return templates.TemplateResponse("add_news.html", {"request": request,
#                                                         "message": message,
#                                                         "token": token,
#                                                         }
#                                       )


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
    
    class Body:
        def __init__(self):
            self.date = date(year=2023, month=7, day=3)
            self.height = 150
            self.weight = 68
            self.age = 35
        
    body = Body()
    
    await repository_calorie.add_calorie(body, db)
    return templates.TemplateResponse("index.html", {"request": request})


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
