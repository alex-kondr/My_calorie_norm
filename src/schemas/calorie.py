import datetime
from typing import Annotated
from fastapi import Form

from pydantic import BaseModel, Field


class Calorie(BaseModel):
    date: Annotated[datetime.date, Form()]
    height: Annotated[float, Form()]
    weight: Annotated[float, Form()]
    age: Annotated[int, Form()]
