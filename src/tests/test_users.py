from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# user registration test

def test_user_register():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "username": "testuser",
            "password": "234556757",
            "email": "test@example.com"
        }
                                
    )
    assert response.status_code == 201

def test_user_invalid_email():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "username": "testuser1",
            "password": "234556757",
            "email": "testexample"
        }
                                
    )
    assert response.status_code == 422

def test_user_duplicate_email():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "username": "testuser2",
            "password": "234556757",
            "email": "test@example.com"
        }
                                
    )
    assert response.status_code == 400

def test_user_duplicate_username():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "username": "testuser",
            "password": "234556757",
            "email": "test3@example.com"
        }
                                
    )
    assert response.status_code == 400

def test_user_missing_username():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "password": "234556757",
            "email": "test4@example.com"
        }
                                
    )
    assert response.status_code == 422

def test_user_missing_email():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "username": "testuser",
            "password": "234556757"
        }
                                
    )
    assert response.status_code == 422

def test_user_missing_name():
    response = client.post(
        "/auth/register/",
    json={

            "username": "testuser2",
            "password": "234556757",
            "email": "test@example.com"
        }
                                
    )
    assert response.status_code == 422


def test_user_missing_password():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "username": "testuser2",
            "email": "test@example.com"
        }
                                
    )
    assert response.status_code == 422

def test_user_password_lenght():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "username": "testuser",
            "password": "23455",
            "email" : "test5@example.com"
        }
                                
    )
    assert response.status_code == 422

def test_user_emapty_value():
    response = client.post(
        "/auth/register/",
    json={
            "name" : "Test User",
            "username": "testuser",
            "password": " ",
            "email" : " "
        }
                                
    )
    assert response.status_code == 422



## login testing

def test_user_login():
        response = client.post(
        "/auth/register/",
        json={
           "name": "Login Test User",
            "username": "unique_login_user", 
            "password": "999999999",  
            "email": "uniquelogin@mail.com"  
        }
                                
    )
        assert response.status_code == 201
        
        login_credential = {
                        "username": "unique_login_user",
                        "password": "999999999",
}
        response = client.post(
                "/auth/login/", data=login_credential)


        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

def test_user_wrong_password():
        response = client.post(
            "/auth/register/",
        json={
               "name": "Login Test User",
                "username": "loginuser", 
                "password": "999999999",  
                "email": "uniquelogin1@mail.com"  
            }
                                    
        )
        assert response.status_code == 201

        login_credential = {
                    "username": "loginuser",
                    "password": "2345567788",
}
        response = client.post("/auth/login/", data=login_credential)
        
        assert response.status_code == 401

def test_user_wrong_username():
        response = client.post(
            "/auth/register/",
        json={
               "name": "Login Test User",
                "username": "loginuser2", 
                "password": "992415786",  
                "email": "uniquelogin2@mail.com"  
            }
                                    
        )
        assert response.status_code == 201

        login_credential = {
                    "username": "loginuser",
                    "password": "992415786",
}
        response = client.post("/auth/login/", data=login_credential)
        
        assert response.status_code == 401

def test_user_missing_username_in_login():
        response = client.post(
            "/auth/register/",
        json={
               "name": "Login Test User",
                "username": "loginuser3", 
                "password": "992415786",  
                "email": "uniquelogin3@mail.com"  
            }
                                    
        )
        assert response.status_code == 201

        login_credential = {
                            "username": "",
                            "password": "992415786",
        }
        response = client.post("/auth/login/", data=login_credential)
                
        assert response.status_code == 422

def test_user_missing_password_in_login():
        response = client.post(
            "/auth/register/",
        json={
               "name": "Login Test User",
                "username": "loginuser4", 
                "password": "992415786",  
                "email": "uniquelogin4@mail.com"  
            }
                                    
        )
        assert response.status_code == 201

        login_credential = {
                            "username": "loginuser4",
                            "password": "",
        }
        response = client.post("/auth/login/", data=login_credential)
                
        assert response.status_code == 422
