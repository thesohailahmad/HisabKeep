import pytest
import uuid
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


@pytest.fixture(scope="module")
def auth_headers():

    unique_id = str(uuid.uuid4())[:8]
    username = f"testuser_{unique_id}"
    password = "testpassword123"
    
    client.post(
        "/auth/register/",
        json={
            "name": "Test User",
            "username": username,
            "password": password,
            "email": f"{username}@example.com"
        }
    )
    

    login_response = client.post(
        "/auth/login/", 
        data={
            "username": username,
            "password": password
        }
    )
    token = login_response.json()["access_token"]
    
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(scope="module")
def auth_headers_B():

    unique_id = str(uuid.uuid4())[:8]
    username = f"testuserb_{unique_id}"
    password = "testpassword123b"
    
    client.post(
        "/auth/register/",
        json={
            "name": "Test User",
            "username": username,
            "password": password,
            "email": f"{username}@example.com"
        }
    )
    

    login_response = client.post(
        "/auth/login/", 
        data={
            "username": username,
            "password": password
        }
    )
    token = login_response.json()["access_token"]
    
    return {"Authorization": f"Bearer {token}"}



@pytest.fixture
def test_expense(auth_headers):

    response = client.post(
        "/expenses/add_expense/",
        headers=auth_headers,
        json={
            "name": "Initial Laptop",
            "category": "Electronics",
            "amount": 50000
        }
    )
    return response.json()


def test_create_expense(auth_headers):
    response = client.post(
        "/expenses/add_expense/",
        headers=auth_headers,
        json={ 
            "name" : "laptop",
            "category":"Electronic Expense",
            "amount" : 48000
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "laptop"
    assert data["category"] == "Electronic Expense"
    assert data["amount"] == 48000

def test_create_expense_without_token():
    response = client.post(
        "/expenses/add_expense/",
        json={
            "name": "Laptop",
            "category": "Electronics",
            "amount": 50000
        }
    )
    assert response.status_code == 401

def test_create_expense_invalid_token():
    response = client.post(
        "/expenses/add_expense/",
        headers={"Authorization": "Bearer fake_token"},
        json={
            "name": "Laptop",
            "category": "Electronics",
            "amount": 50000
        }
    )
    assert response.status_code == 401


def test_view_all_expenses(auth_headers, test_expense):
    response = client.get("/expenses/View_expense/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1 

def test_view_all_expenses_unauthorized():
    response = client.get("/expenses/View_expense/")
    assert response.status_code == 401


def test_view_single_expense(auth_headers, test_expense):
    expense_id = test_expense["id"]
    response = client.get(f"/expenses/View_expense/{expense_id}", headers=auth_headers)
    
    assert response.status_code == 200
    assert response.json()["id"] == expense_id
    assert response.json()["name"] == test_expense["name"]
    assert response.json()["amount"] == test_expense["amount"]

def test_view_single_expense_not_found(auth_headers):
    response = client.get("/expenses/View_expense/999999", headers=auth_headers)
    assert response.status_code == 404
    assert response.json()["detail"] == "Expense with 999999 id not found"

def test_view_all_single_expenses_unauthorized(test_expense):
    expense_id = test_expense["id"]
    response = client.get(f"/expenses/View_expense/{expense_id}")
    assert response.status_code == 401


def test_update_expense(auth_headers, test_expense):
    expense_id = test_expense["id"]
  
    response = client.put(
        f"/expenses/Update_expense/{expense_id}",
        headers=auth_headers,
        json={
            "amount": 45000, 
            "name": "Discounted Laptop"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 45000
    assert data["name"] == "Discounted Laptop"
    assert data["category"] == test_expense["category"] 

def test_update_expense_not_found(auth_headers):
    response = client.put(
        "/expenses/Update_expense/999999",
        headers=auth_headers,
        json={"amount": 100}
    )
    assert response.status_code == 404


def test_update_expenses_unauthorized(test_expense):
    expense_id = test_expense["id"]
    response = client.put(f"/expenses/Update_expense/{expense_id}")
    assert response.status_code == 401




def test_delete_expense(auth_headers, test_expense):
    expense_id = test_expense["id"]
 
    delete_response = client.delete(f"/expenses/delete_expense/{expense_id}", 
    headers=auth_headers
    )
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == expense_id

## verify it no longer to retriev
    get_response = client.get(f"/expenses/View_expense/{expense_id}", headers=auth_headers)
    assert get_response.status_code == 404

def test_delete_expense_not_found(auth_headers):
    response = client.delete("/expenses/delete_expense/999999", headers=auth_headers)
    assert response.status_code == 404


def test_delete_expense_unauthorized(test_expense):
    expense_id = test_expense["id"]
    response = client.delete(f"/expenses/delete_expense/{expense_id}")
    assert response.status_code == 401

def test_user_b_cannot_view_user_a_expense(auth_headers_B,test_expense):
    expense_id = test_expense["id"]

    response = client.get(
        f"/expenses/View_expense/{expense_id}",
        headers=auth_headers_B
    )

    assert response.status_code == 404

def test_user_b_cannot_update_user_a_expense(auth_headers_B,test_expense):

    expense_id = test_expense["id"]

    response = client.put(
        f"/expenses/Update_expense/{expense_id}",
        headers=auth_headers_B,
        json={
            "name": "Hacked Expense",
            "amount": 1
        }
    )
    assert response.status_code == 404

def test_user_b_cannot_delete_user_a_expense(auth_headers_B,test_expense):

    expense_id = test_expense["id"]

    response = client.delete(
        f"/expenses/delete_expense/{expense_id}",
        headers=auth_headers_B
    )

    assert response.status_code == 404

def test_user_b_cannot_see_user_a_expenses(test_expense, auth_headers_B):
    response = client.get(
        "/expenses/View_expense/",
        headers=auth_headers_B
    )

    assert response.status_code == 200

    expenses = response.json()

    expense_ids = [expense["id"] for expense in expenses]

    assert test_expense["id"] not in expense_ids

def test_create_expense_negative_amount(auth_headers):
      
    response = client.post(
        f"/expenses/add_expense/",
        headers=auth_headers,
        json={
            "amount": -200,
            "name": "Discounted Laptop"
        }
    )
    assert response.status_code == 422

def test_create_expense_empty_name(auth_headers):

    response = client.post(
        f"/expenses/add_expense/",
        headers=auth_headers,
        json={
            "amount": 45000, 
            "category": "Laptop"
        }
    )
    assert response.status_code == 422

def test_create_expense_empty_amount(auth_headers):

    response = client.post(
        f"/expenses/add_expense/",
        headers=auth_headers,
        json={
            "name" : "Laptop",
            "category": "Electronic"
        }
    )
    assert response.status_code == 422


