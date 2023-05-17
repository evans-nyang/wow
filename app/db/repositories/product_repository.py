from app.db.models.product import Product
from app.db.base import Session


class ProductRepository:
    @staticmethod
    def create_product(product_data):
        product = Product(**product_data)
        session = Session()
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    @staticmethod
    def update_product(product, updated_data):
        for key, value in updated_data.items():
            setattr(product, key, value)
        session = Session()
        session.commit()
        session.refresh(product)
        return product
    
    @staticmethod
    def delete_product(product):
        session = Session()
        session.delete(product)
        session.commit()

    @staticmethod
    def get_product_by_id(product_id):
        session = Session()
        return session.query(Product).get(product_id)

    @staticmethod
    def get_all_products():
        session = Session()
        return session.query(Product).all()
