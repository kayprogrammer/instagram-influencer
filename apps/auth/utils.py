from datetime import datetime, timedelta
import jwt
import random
import string

from setup.settings import SECRET_KEY

from . models import User, Jwt

# generate random string
def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# generate access token based on user's id
def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.utcnow() + timedelta(minutes=5), **payload},
        SECRET_KEY,
        algorithm="HS256"
    )

# generate random refresh token
def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.utcnow() + timedelta(hours=24), "data": get_random(10)},
        SECRET_KEY,
        algorithm="HS256"
    )

# verify refresh token
def verify_token(token):
    
    try:
        decoded_data = jwt.decode(
            token, SECRET_KEY, algorithms=["HS256"])
        return True
    except:
        return False

# deocde access token from header
def decodeJWT(db, token):
    if not token:
        return None

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidSignatureError:
        return None

    if decoded:
        user = db.query(User).filter_by(id=decoded["user_id"]).first()
        
        if user:
            jwt_obj = db.query(Jwt).filter_by(user_id=user.id).first()
            if not jwt_obj: # to confirm the validity of the token
                return None
            return user
        return None
