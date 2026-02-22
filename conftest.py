import pytest
import json

@pytest.fixture(scope="session")
def test_data():
    with open("test_data/credentials.json") as f:
        return json.load(f)

@pytest.fixture
def login_page(page):
    from pages.login_page import LoginPage
    page.goto("/")  # base URL is set in pytest.ini
    return LoginPage(page)