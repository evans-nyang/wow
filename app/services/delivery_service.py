from app.db.repositories.delivery_repository import DeliveryRepository


class DeliveryService:
    def __init__(self):
        self.delivery_repository = DeliveryRepository()

    def create_delivery(self, delivery_data):
        return self.delivery_repository.create_delivery(delivery_data)

    def update_delivery(self, delivery_id, updated_data):
        delivery = self.get_delivery_by_id(delivery_id)
        if delivery:
            return self.delivery_repository.update_delivery(delivery, updated_data)
        return None

    def get_delivery_by_id(self, delivery_id):
        return self.delivery_repository.get_delivery_by_id(delivery_id)

    def get_all_deliveries(self):
        return self.delivery_repository.get_all_deliveries()
