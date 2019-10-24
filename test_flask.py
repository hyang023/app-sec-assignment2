import pytest

import app

@pytest.fixture
def app():
    app = app.create_app()
    app.debug = True
    return app.test_client()

def test_hello_world(app):
    res = app.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Hello World" in res.data
