from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app import crud, models, schemas

router = APIRouter()

@router.post("/users", response_model=models.UserInDB)
def create_user(user: schemas.UserCreate, db: Session = Depends(SessionLocal)):
    return crud.create_user(db=db, user=user)

@router.get("/users/{email}", response_model=models.UserInDB)
def read_user(email: str, db: Session = Depends(SessionLocal)):
    user = crud.get_user_by_email(db=db, email=email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
