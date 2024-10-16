from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from schemas import UserBase, UserDisplay
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

#create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

#read all user
@router.get('/',response_model = List[UserDisplay])
def get_all_users(db:Session = Depends(get_db)):
    return db_user.get_all_users(db)

#read one user
@router.get('/{id}', response_model=UserDisplay)
def get_one_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_one_user(db,id)
    

#update user
@router.post('/{id}/update')
def update_user(id: int,request:UserBase,  db: Session = Depends(get_db) ):
    return db_user.update_user(db, request, id)

#delete user
@router.get('/{id}/delete')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db,id)


