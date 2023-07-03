from sqlalchemy import Column, Integer, func, Float, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Calorie(Base):
    __tablename__ = 'Calorie'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    height = Column(Float, default=0)
    weight = Column(Float, default=0)
    age = Column(Integer, default=0)
    calorie = Column(Float, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
