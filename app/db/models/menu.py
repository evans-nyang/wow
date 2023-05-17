from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from app.db.base import Base

class Item(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Numeric)
    description = Column(String)
