from fastapi import APIRouter

from app.services.review_service import ReviewService

router = APIRouter()
review_service = ReviewService()


@router.get("/reviews")
def get_reviews():
    reviews = review_service.get_all_reviews()
    return {"reviews": reviews}


@router.get("/reviews/{review_id}")
def get_review(review_id: int):
    review = review_service.get_review_by_id(review_id)
    if review:
        return review
    return {"error": "review not found"}


@router.post("/reviews")
def create_review(review_data: dict):
    review = review_service.create_review(review_data)
    return review


@router.put("/reviews/{review_id}")
def update_review(review_id: int, updated_data: dict):
    review = review_service.update_review(review_id, updated_data)
    if review:
        return review
    return {"error": "review not found"}
