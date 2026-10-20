import requests
import pytest
from clients.api_manager import ApiManager
from utils.data_generator import DataGenerator


@pytest.fixture(scope="session")
def session():
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(session):  # session — фикстура
    return ApiManager(session=session)  # session — объект requests.Session


@pytest.fixture(scope="function")
def test_user():
    password = DataGenerator.generate_random_password()
    return {
        "email": DataGenerator.generate_random_email(),
        "fullName": DataGenerator.generate_random_name(),
        "password": password,
        "passwordRepeat": password,
        "roles": ["USER"]
    }


@pytest.fixture(scope="function")
def registered_user(api_manager, test_user):
    response = api_manager.auth_api.register_user(test_user).json()
    test_user["id"] = response["id"]
    return test_user


@pytest.fixture(scope="function")
def authenticated_user(api_manager, test_user):
    register_response = api_manager.auth_api.register_user(test_user)
    register_data = register_response.json()
    test_user["id"] = register_data["id"]
    api_manager.auth_api.authenticate(user_creds=(test_user["email"], test_user["password"]))
    return test_user
