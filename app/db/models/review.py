# db/models/review.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # Define the relationship with the User model
    user = relationship("User", backref="reviews")
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    # Define the relationship with the Product model
    product = relationship("Product", backref="reviews")
    rating = Column(Float, nullable=False)
    comment = Column(String(255))
    # Add more columns as needed

    def __repr__(self):
        return f"<Review(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, rating={self.rating})>"
