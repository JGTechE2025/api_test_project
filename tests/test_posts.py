import pytest
from apis.posts_api import PostsAPI


@pytest.fixture
def api():
    return PostsAPI()


def test_get_all_posts(api):
    res = api.get_all_posts()
    assert res.status_code == 200
    assert isinstance(res.json(), list)  # 驗證返回結果是個列表


def test_get_single_post(api):
    res = api.get_post_by_id(1)
    assert res.status_code == 200
    assert res.json()["id"] == 1  # 驗證返回的ID是否正確


def test_create_post(api):
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    res = api.create_post(new_post)
    assert res.status_code == 201
    assert res.json()["title"] == "foo"  # 驗證返回的title是否正確


def test_get_nonexistent_post(api):
    res = api.get_post_by_id(9999)  # 假設此ID不存在
    assert res.status_code == 404  # 驗證返回404錯誤


def test_create_post_invalid_data(api):
    invalid_post = {"title": "foo", "userId": 1}  # 沒有body字段
    res = api.create_post(invalid_post)
    assert res.status_code == 404  # 驗證返回404錯誤，因為缺少必填字段 (api實際回傳201)

