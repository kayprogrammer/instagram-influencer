from fastapi import status, Depends
from sqlalchemy.orm import Session

from setup.main import client
from setup.database import get_db

from . routes import get_current_user

def test_provide_details():
    #login
    login_response = client.post("/api/v1/auth/login", json={"email": "example@email.com", "password": "password"})
    token = login_response.json()['access']

    # provide details
    response = client.post("/api/v1/influencers/provide-details", 
        headers={'Authorization': f'Bearer {token}'}, 
        json={"username": "aslama", "followers_count": 29, "bio": "Im there"}
    )
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"influencer": {"username": "aslama", "followers_count": 29, "bio": "Im there"}, "message": "Influencer profile updated"}

def test_search():
    response = client.get("/api/v1/influencers/search")
    assert response.status_code == status.HTTP_200_OK
