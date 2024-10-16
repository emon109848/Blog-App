from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user
from typing import Optional
from datetime import datetime,timedelta
from jose import JWTError, jwt

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')
SECRET_KEY = 'a943f5803ce91f0c57fc5f9ef6563d88eac611ebff346d0acf1e99cd8300b821'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta]= None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def get_current_user(db:Session=Depends(get_db), token:str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db_user.get_user_by_username(db,username)
    
    if username is None:
        raise credentials_exception
    
    return user