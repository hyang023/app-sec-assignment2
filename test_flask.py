import pytest

import app

@pytest.fixture
def app():
    app = app.create_app()
    app.debug = True
    return app.test_client()
