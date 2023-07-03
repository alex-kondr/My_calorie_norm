from sqlalchemy.orm import Session
from sqlalchemy import desc

from src.database.models import Calorie


def calculate_calorie(height, weight, age):
    return 655.1 + 9.563 * height + 1.85 * weight - 4.767 * age


async def get_calories(db: Session) -> list:
    return db.query(Calorie).order_by(desc(Calorie.created_at)).all()


async def add_calorie(body, db: Session):
    body.calorie = calculate_calorie(body.height, body.weight, body.age)
    print(body.calorie)
    calorie = Calorie(**body.__dict__)
    db.add(calorie)
    db.commit()
    db.refresh(calorie)
    return calorie


# async def delete_news(news_id: int, db: Session):
#     db.query(Content).filter_by(id=news_id).delete()
#     db.commit()
