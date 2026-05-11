import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]

def test_signup_for_activity():
    email = "testuser@mergington.edu"
    activity = "Chess Club"
    # Remove if already present
    client.delete(f"/activities/{activity}/participants", params={"email": email})
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert response.status_code == 200
    data = response.json()
    assert f"Signed up {email} for {activity}" in data["message"]
    # Clean up
    client.delete(f"/activities/{activity}/participants", params={"email": email})

def test_unregister_from_activity():
    email = "testuser2@mergington.edu"
    activity = "Chess Club"
    # Ensure user is signed up
    client.post(f"/activities/{activity}/signup", params={"email": email})
    response = client.delete(f"/activities/{activity}/participants", params={"email": email})
    assert response.status_code == 200
    data = response.json()
    assert f"Unregistered {email} from {activity}" in data["message"]
