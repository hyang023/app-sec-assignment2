import pytest

import app

@pytest.fixture
def apptest():
    apptest = app.create_app()
    apptest.debug = True
    return apptest.test_client()

def test_hello_world(app):
    res = apptest.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Hello World" in res.data
