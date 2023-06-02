from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import datetime

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    # Define the relationship with the Order model
    order = relationship("Order", backref="payments")
    status = Column(Enum('pending', 'paid', 'failed'), nullable=False)
    # Add more columns as needed
    # paymentmethod = Column(String, nullable=False)
    # amount = Column(Integer, nullable=False)
    # created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Payment(id={self.id}, order_id={self.order_id}, status='{self.status}')>"
