from app.db.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def create_product(self, product_data):
        return self.product_repository.create_product(product_data)

    def update_product(self, product_id, updated_data):
        product = self.get_product_by_id(product_id)
        if product:
            return self.product_repository.update_product(product, updated_data)
        return None

    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            self.product_repository.delete_product(product)

    def get_product_by_id(self, product_id):
        return self.product_repository.get_product_by_id(product_id)

    def get_all_products(self):
        return self.product_repository.get_all_products()
