from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # Define the relationship with the User model
    user = relationship("User", backref="orders")
    # Add more columns as needed

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id})>"
