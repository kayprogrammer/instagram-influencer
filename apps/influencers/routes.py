from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import or_
from sqlalchemy.orm import Session
from typing import List

from . schemas import InfluencersSchema
from apps.auth.models import User
from apps.auth.routes import get_current_user

from setup.database import get_db

influencersrouter = APIRouter(tags=['influencers'])

@influencersrouter.post('/provide-details')
async def provide_details(
        influencer: InfluencersSchema, 
        db: Session = Depends(get_db), 
        user: User = Depends(get_current_user), 
        status_code = status.HTTP_200_OK
    ):

    duplicate_user = db.query(User).filter_by(username=influencer.username).filter(User.id != user.id).first()

    if duplicate_user: # check if a user already has such username
        raise HTTPException(status_code=400, detail="Another user exists with that username")

    # update logged in user details with his/her instagram details.
    user.username = influencer.username
    user.followers_count = influencer.followers_count
    user.bio = influencer.bio

    db.commit()
    return {'influencer': influencer, 'message': 'Influencer profile updated'}

@influencersrouter.get('/search', response_model = List[InfluencersSchema])
async def search(
        text: str = None, 
        max_followers: int = None, 
        min_followers: int = None, 
        db: Session = Depends(get_db), 
        status_code = status.HTTP_200_OK
    ):

    # filter all influencers, ensuring that they have a usrename and followers count
    influencers = db.query(User).filter(User.username != None, User.followers_count != None)

    # all conditionals below checks if the respected query params exists in endpoint
    if text:
        return influencers.filter(
            or_(User.username.contains(text), User.bio.contains(text))
        ).order_by(User.created_at).all()

    if max_followers:
        return influencers.filter(
            User.followers_count <= max_followers
        ).order_by(User.created_at).all()

    if min_followers:
        return influencers.filter(
            User.followers_count >= min_followers
        ).order_by(User.created_at).all()

    return influencers.order_by(User.created_at).all()
