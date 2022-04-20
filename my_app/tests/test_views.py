
from flask import Flask

import pytest


from my_app.views import app





def test_index():

    tester = app.test_client()
    response = tester.get('/', content_type = 'html/text')
    assert response.status_code == 200

# def test_result():
#     tester = app.test_client()
#     response = tester.get('result', content_type = 'html/text')
#     assert response.status_code == 200

@pytest.fixture
def client():
    app.config["TESTING"] = True
    yield app.test_client()