import pytest
import sys
import allure
sys.path.append('./lib')
from api import ApiMethods
from assertions import Assertions



"""Тестирвоание аутентификации пользователя в системе"""


@allure.epic("Тестирование пользовательской аутентификации")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin():

    @allure.feature("Тест аутентификации с валидными данными")
    def test_login_valid_data(self, set_for_login):

        body = {

            "password": "testpassword",
            "username": "testname_login"

        }
        request = ApiMethods.login_user(body)
        Assertions.check_status_code(request, 200)
        Assertions.check_json_field(request, "token")
        
        

    @allure.feature("Тест аутентификации с невалидными данными")
    @allure.description("Используется неверный пароль")
    def test_login_invalid_data(self):
        
        body = {

            "password": "wrongpassword",
            "username": "testname_login"

        }
        request = ApiMethods.login_user(body)
        print(request.text)
        Assertions.check_status_code(request, 403)
        Assertions.check_json_fields(request, ("code", "message"))

    @allure.feature("Тест аутентификации без указания пароля")
    def test_login_without_password(self):
            
        body = {

            "username": "testname_login"

        }
        request = ApiMethods.login_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
        Assertions.check_json_fields(request, ("code", "message"))

    @allure.feature("Тест аутентификации без указания логина/имени пользователя")
    def test_login_without_username(self):

        body = {

            "password": "testpassword"

        }
        request = ApiMethods.login_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
        Assertions.check_json_fields(request, ("code", "message"))

    @allure.feature("Тест аутентификации без входных данных")
    def test_login_empty_data(self):

        body = {
        }
        request = ApiMethods.login_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
        Assertions.check_json_fields(request, ("code", "message"))

    @allure.feature("Тест аутентификации с применением длинного токена/'запомнить меня'")
    def test_login_long_token(self):

        body = {

            "long_token": True,
            "password": "testpassword",
            "username": "testname_login"

        }
        request = ApiMethods.login_user(body)
        print(request.text)
        Assertions.check_status_code(request, 200)
        Assertions.check_json_field(request, "token")


        



                                    

