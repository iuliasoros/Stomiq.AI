from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stomiq.AI API")

class UserCreate(BaseModel):
    email: str
    phone: str
    password: str
    role: str

@app.post("/signup/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifică dacă emailul există deja
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email deja înregistrat")
    
    # Creează contul
    new_user = models.User(
        email=user.email,
        phone=user.phone,
        role=user.role,
        hashed_password=user.password 
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"mesaj": "Cont creat cu succes!", "email": new_user.email, "rol": new_user.role}