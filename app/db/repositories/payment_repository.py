from app.db.models.payment import Payment
from app.db.base import Session


class PaymentRepository:
    @staticmethod
    def create_payment(payment_data):
        payment = Payment(**payment_data)
        session = Session()
        session.add(payment)
        session.commit()
        session.refresh(payment)
        return payment

    @staticmethod
    def update_payment(payment, updated_data):
        for key, value in updated_data.items():
            setattr(payment, key, value)
        session = Session()
        session.commit()
        session.refresh(payment)
        return payment

    @staticmethod
    def get_payment_by_id(payment_id):
        session = Session()
        return session.query(Payment).get(payment_id)

    @staticmethod
    def get_all_payments():
        session = Session()
        return session.query(Payment).all()
