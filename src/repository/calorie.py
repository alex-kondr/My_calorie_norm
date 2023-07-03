import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc

from src.database.models import Calorie


def calculate_calorie(height, weight, age):
    return round(655.1 + 9.563 * weight + 1.85 * height - 4.767 * age, 1)


async def get_calories(db: Session) -> list:
    return db.query(Calorie).order_by(desc(Calorie.created_at)).all()


async def add_calorie(date: datetime.date,
                                 height: float, 
                                 weight:float, 
                                 age: int, 
                                 db: Session):
    
    calculate = calculate_calorie(height, weight, age)
    calorie = Calorie(date=date, height=height, weight=weight, age=age, calorie=calculate)
    db.add(calorie)
    db.commit()
    db.refresh(calorie)
    return calorie


async def delete_calorie(calorie_id: int, db: Session):
    db.query(Calorie).filter_by(id=calorie_id).delete()
    db.commit()
