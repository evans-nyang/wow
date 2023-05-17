# db/models/product.py

from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255))
    # Add more columns as needed

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
