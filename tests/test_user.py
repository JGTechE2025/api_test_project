import pytest
from apis.users_api import UsersAPI


@pytest.fixture
def api():
    return UsersAPI()


def test_get_all_users(api):
    res = api.get_all_users()
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_get_user_by_id(api):
    res = api.get_user_by_id(1)
    assert res.status_code == 200
    assert res.json()["id"] == 1


def test_create_user(api):
    new_user = {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }
    res = api.create_user(new_user)
    assert res.status_code == 201  # 請求已成功處理，並且已經創建了一個新的資源
    assert res.json()["name"] == "Test User"


def test_update_user(api):
    updated_data = {
        "name": "Updated User",
        "username": "updateduser",
        "email": "updated@example.com"
    }
    res = api.update_user(1, updated_data)
    assert res.status_code == 200  # 請求已成功處理，並且返回了所請求的資源
    assert res.json()["name"] == "Updated User"


def test_delete_user(api):
    res = api.delete_user(1)
    assert res.status_code == 200
