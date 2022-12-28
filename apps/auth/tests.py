from fastapi import status, Depends
from setup.main import client
from . routes import get_current_user

def test_register():
    response = client.post("/api/v1/auth/register", json={"email": "example@email.com", "password": "password"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"user": {"email": "example@email.com", "password": "password"}, "message": "Registration successful"}

def test_login():
    response = client.post("/api/v1/auth/login", json={"email": "example@email.com", "password": "password"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"access": response.json()['access'], "refresh": response.json()['refresh']}

def test_refresh():
    #login
    login_response = client.post("/api/v1/auth/login", json={"email": "example@email.com", "password": "password"})

    #refresh
    response = client.post("/api/v1/auth/refresh", json={"refresh": login_response.json()['refresh']})
    assert response.status_code == 201
    assert response.json() == {"access": response.json()['access'], "refresh": response.json()['refresh']}

def test_logout():
    #login
    login_response = client.post("/api/v1/auth/login", json={"email": "example@email.com", "password": "password"})
    token = login_response.json()['access']

    #logout
    response = client.get("/api/v1/auth/logout", headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 200
    assert response.json() == {"message": 'Logged out successfully'}
