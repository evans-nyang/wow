from app.db.models.review import Review
from app.db.base import SessionLocal


class ReviewRepository:
    @staticmethod
    def create_review(review_data):
        review = Review(**review_data)
        session = SessionLocal()
        session.add(review)
        session.commit()
        session.refresh(review)
        return review

    @staticmethod
    def update_review(review, updated_data):
        for key, value in updated_data.items():
            setattr(review, key, value)
        session = SessionLocal()
        session.commit()
        session.refresh(review)
        return review

    @staticmethod
    def get_review_by_id(review_id):
        session = SessionLocal()
        return session.query(Review).get(review_id)

    @staticmethod
    def get_all_reviews():
        session = SessionLocal()
        return session.query(Review).all()
