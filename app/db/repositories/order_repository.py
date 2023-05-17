from app.db.models.order import Order
from app.db.base import Session


class OrderRepository:
    @staticmethod
    def create_order(order_data):
        order = Order(**order_data)
        session = Session()
        session.add(order)
        session.commit()
        session.refresh(order)
        return order

    @staticmethod
    def update_order(order, updated_data):
        for key, value in updated_data.items():
            setattr(order, key, value)
        session = Session()
        session.commit()
        session.refresh(order)
        return order
    
    @staticmethod
    def delete_order(order):
        session = Session()
        session.delete(order)
        session.commit()

    @staticmethod
    def get_order_by_id(order_id):
        session = Session()
        return session.query(Order).get(order_id)

    @staticmethod
    def get_all_orders():
        session = Session()
        return session.query(Order).all()
