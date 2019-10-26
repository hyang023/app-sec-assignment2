import pytest

import app

@pytest.fixture
def app():
    app = main.create_app()
    app.debug = True
    return app.test_client()
