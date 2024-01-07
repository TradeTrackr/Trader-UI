from flask import Flask, request, redirect, abort, session
import datetime
from functools import wraps
from jose import jwt, JWTError
from trader_ui.config import Config

# Create a decorator for token required
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Check if token is passed in the headers
        if 'access_token' not in session:
            session.clear()
            return redirect("./login")
        
        token = session['access_token']

        try:
            # Decode the token
            payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[Config.ALGORITHM])
            current_user = payload.get("sub")
            if current_user is None:
                raise JWTError("Invalid token payload")

        except JWTError as e:
            session.clear()
            return redirect("./login")

        return f(*args, **kwargs)

    return decorated

class Authentication(object):
    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()
        to_encode.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=int(Config.ACCESS_TOKEN_EXPIRE_MINUTES))})
        encoded_jwt = jwt.encode(to_encode, Config.JWT_SECRET_KEY, algorithm=Config.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def create_refresh_token(data: dict, expires_delta: datetime.timedelta = None):
        to_encode = data.copy()
        if expires_delta is None:
            expires_delta = datetime.timedelta(days=int(Config.REFRESH_TOKEN_EXPIRE_DAYS))
        expire = datetime.datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Config.JWT_SECRET_KEY, algorithm=Config.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def validate_refresh_token(refresh_token: str):
        try:
            payload = jwt.decode(refresh_token, Config.JWT_SECRET_KEY, algorithms=[Config.ALGORITHM])
            id: str = payload.get("sub")
            if id is None:
                abort(400, description="Invalid refresh token")
            return id
        except JWTError:
            abort(403, description="Could not validate credentials")

