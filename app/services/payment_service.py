from app.db.repositories.payment_repository import PaymentRepository


class PaymentService:
    def __init__(self):
        self.payment_repository = PaymentRepository()

    def create_payment(self, payment_data):
        return self.payment_repository.create_payment(payment_data)

    def update_payment(self, payment_id, updated_data):
        payment = self.get_payment_by_id(payment_id)
        if payment:
            return self.payment_repository.update_payment(payment, updated_data)
        return None

    def get_payment_by_id(self, payment_id):
        return self.payment_repository.get_payment_by_id(payment_id)

    def get_all_payments(self):
        return self.payment_repository.get_all_payments()
