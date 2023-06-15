import pytest
import sys
sys.path.append('./lib')
from api import ApiMethods 



"""Тестовые конфигурации"""


@pytest.fixture()
def set_for_login():
    body = {

    "email": "testloginmail@gmail.com",
    "password": "testpassword",
    "username": "testname_login"

    }
    request = ApiMethods.register_new_user(body)


@pytest.fixture()
def set_for_project(): 
    body_reg = {

    "email": "testprojectmail@gmail.com",
    "password": "testpassword",
    "username": "testname_project"

    }
    request_reg = ApiMethods.register_new_user(body_reg)


    body_log = {

    "password": "testpassword",
    "username": "testname_project"

    }
    request_log = ApiMethods.login_user(body_log)
    response_json = request_log.json()
    token = response_json.get("token")
    return token


@pytest.fixture()
def set_for_user(): 
    body_reg = {

    "email": "testusermail@gmail.com",
    "password": "testpassword",
    "username": "testname_user"

    }
    request_reg = ApiMethods.register_new_user(body_reg)


    body_log = {

    "password": "testpassword",
    "username": "testname_user"

    }
    request_log = ApiMethods.login_user(body_log)
    response_json = request_log.json()
    token = response_json.get("token")
    return token


@pytest.fixture()
def set_for_password(): 
    body_reg = {

    "email": "testpasswordmail@gmail.com",
    "password": "testpassword",
    "username": "testname_password"

    }
    request_reg = ApiMethods.register_new_user(body_reg)


    body_log = {

    "password": "testpassword",
    "username": "testname_password"

    }
    request_log = ApiMethods.login_user(body_log)
    response_json = request_log.json()
    print(response_json)
    token = response_json.get("token")
    return token