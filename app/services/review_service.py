from app.db.repositories.review_repository import ReviewRepository


class ReviewService:
    def __init__(self):
        self.review_repository = ReviewRepository()

    def create_review(self, review_data):
        return self.review_repository.create_review(review_data)

    def update_review(self, review_id, updated_data):
        review = self.get_review_by_id(review_id)
        if review:
            return self.review_repository.update_review(review, updated_data)
        return None

    def get_review_by_id(self, review_id):
        return self.review_repository.get_review_by_id(review_id)

    def get_all_reviews(self):
        return self.review_repository.get_all_reviews()
