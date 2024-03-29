from app.db.models.delivery import Delivery
from app.db.base import SessionLocal


class DeliveryRepository:
    @staticmethod
    def create_delivery(delivery_data):
        delivery = Delivery(**delivery_data)
        session = SessionLocal()
        session.add(delivery)
        session.commit()
        session.refresh(delivery)
        return delivery

    @staticmethod
    def update_delivery(delivery, updated_data):
        for key, value in updated_data.items():
            setattr(delivery, key, value)
        session = SessionLocal()
        session.commit()
        session.refresh(delivery)
        return delivery

    @staticmethod
    def get_delivery_by_id(delivery_id):
        session = SessionLocal()
        return session.query(Delivery).get(delivery_id)

    @staticmethod
    def get_all_deliveries():
        session = SessionLocal()
        return session.query(Delivery).all()
