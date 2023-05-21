from app.db.repositories.order_repository import OrderRepository


class OrderService:
    def __init__(self):
        self.order_repository = OrderRepository()

    def create_order(self, order_data):
        return self.order_repository.create_order(order_data)

    def update_order(self, order_id, updated_data):
        order = self.get_order_by_id(order_id)
        if order:
            return self.order_repository.update_order(order, updated_data)
        return None

    def delete_order(self, order_id):
        order = self.get_order_by_id(order_id)
        if order:
            self.order_repository.delete_order(order)

    def get_order_by_id(self, order_id):
        return self.order_repository.get_order_by_id(order_id)

    def get_all_orders(self):
        return self.order_repository.get_all_orders()
