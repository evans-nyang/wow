from app.db.base import SessionLocal
# from app.db.base import Base
from app.db.models.menu import Item


class ItemRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def get_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(Item).offset(skip).limit(limit).all()

    def get_item(self, item_id: int):
        return self.db.query(Item).filter(Item.id == item_id).first()

    def create_item(self, item: dict):
        db_item = Item(**item)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
