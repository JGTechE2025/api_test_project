import pytest
from apis.comments_api import CommentsAPI


@pytest.fixture
def api():
    return CommentsAPI()


def test_get_all_comments(api):
    res = api.get_all_comments()
    assert res.status_code == 200


def test_get_comment_by_id(api):
    res = api.get_comment_by_id(1)
    assert res.status_code == 200
    assert res.json()["id"] == 1
