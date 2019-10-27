import pytest

import app

@pytest.fixture
def apptest():
    apptest = app.create_app()
    apptest.debug = True
    return apptest.test_client()

def test_hello_world(apptest):
    res = apptest.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Hello, World!" in res.data

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def test_hello_world(apptest):
    res = apptest.get("/login")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Login" in res.data
