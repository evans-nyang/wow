from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base

class Delivery(Base):
    __tablename__ = 'deliveries'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    # Define the relationship with the Order model
    order = relationship("Order", backref="delivery")
    status = Column(Enum('pending', 'in_transit', 'delivered'), nullable=False)
    # Add more columns as needed

    def __repr__(self):
        return f"<Delivery(id={self.id}, order_id={self.order_id}, status='{self.status}')>"
