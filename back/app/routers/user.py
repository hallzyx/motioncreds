from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import  User
from app.schemas.user import UserCreate, UserRead

router=APIRouter(prefix="/user", tags=["user"])



@router.post("/", response_model=UserRead)
def create_user(user_in:UserCreate, db:Session=Depends(get_db)):
    user_exists=db.query(User).filter(User.email==user_in.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Este correo ya existe")
    
    new_user= User(name=user_in.name,email=user_in.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id=int, db: Session=Depends(get_db)):
    db_user=db.query(User).filter(User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="El usuario no existe, id invalida")
    return db_user


@router.post("/{user_id}/gesture")
def register_gesture(user_id: int, gesture: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Suponiendo que tu modelo User tiene un campo gesture_data (tipo JSON)
    user.gesture_data = gesture
    db.commit()
    db.refresh(user)
    return {"msg": "Gesture registered successfully", "gesture_size": len(gesture)}