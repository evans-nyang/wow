from app.db.models.product import Product
from app.db.base import SessionLocal


class ProductRepository:
    @staticmethod
    def create_product(product_data):
        product = Product(**product_data)
        session = SessionLocal()
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    @staticmethod
    def update_product(product, updated_data):
        for key, value in updated_data.items():
            setattr(product, key, value)
        session = SessionLocal()
        session.commit()
        session.refresh(product)
        return product
    
    @staticmethod
    def delete_product(product):
        session = SessionLocal()
        session.delete(product)
        session.commit()

    @staticmethod
    def get_product_by_id(product_id):
        session = SessionLocal()
        return session.query(Product).get(product_id)

    @staticmethod
    def get_all_products():
        session = SessionLocal()
        return session.query(Product).all()
