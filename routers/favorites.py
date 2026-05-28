from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Favorites
from schemas import FavoriteCreate, FavoriteResponse

router = APIRouter(prefix="/favs", tags=["favorites"])

@router.get("/", response_model=List[FavoriteResponse])
def get_favorites(email: str, db: Session = Depends(get_db)):
    return db.query(Favorites).filter(Favorites.email == email).all()

@router.post("/", response_model=FavoriteResponse, status_code=201)
def create_favorite(fav: FavoriteCreate, db: Session = Depends(get_db)):
    new_fav = Favorites(**fav.model_dump())
    db.add(new_fav)
    db.commit()
    db.refresh(new_fav)
    return new_fav

@router.put("/{fav_id}", response_model=FavoriteResponse)
def update_favorite(fav_id: int, fav: FavoriteCreate, db: Session = Depends(get_db)):
    db_fav = db.query(Favorites).filter(Favorites.id == fav_id).first()
    if db_fav is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    for key, value in fav.model_dump().items():
        setattr(db_fav, key, value)
    db.commit()
    db.refresh(db_fav)
    return db_fav

@router.delete("/{fav_id}", status_code=204)
def delete_favorite(fav_id: int, db: Session = Depends(get_db)):
    db_fav = db.query(Favorites).filter(Favorites.id == fav_id).first()
    if db_fav is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    db.delete(db_fav)
    db.commit()