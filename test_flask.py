import pytest

import app

@pytest.fixture
def apptest():
    apptest = app.create_app()
    apptest.debug = True
    return apptest.test_client()
