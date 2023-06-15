import sys
import pytest
sys.path.append('./lib')
import allure
from api import ApiMethods
from assertions import Assertions



"""Тестирование функциональности изменения пароля"""


"""Сброс пароля до прежнего значения"""
def reset_password():
    body = {
    "new_password": "testpassword",
    "old_password": "newtestpassword"
    }
    request = ApiMethods.change_password(token, body)

@allure.epic("Тестирование изменения пароля")
@allure.severity(allure.severity_level.NORMAL)
class TestChangePassword():

    @allure.feature("Тест изменения пароля с валидными данными")
    # @pytest.mark.run(order=1)
    def test_change_password(self, set_for_password):
        global token
        token = set_for_password
        body = {
        "new_password": "newtestpassword",
        "old_password": "testpassword"
        }
        request = ApiMethods.change_password(token, body)
        print(request.text)
        Assertions.check_status_code(request, 200)
        Assertions.check_json_field(request, "message")
        Assertions.check_json_field_value(request, "message", "The password was updated successfully.")
        
    @allure.feature("Тест изменения пароля с невалидными данными")
    @allure.description("Тест изменения пароля с неверно указанным старым паролем")
    # @pytest.mark.run(order=3)
    def test_change_wrong_password(self):
        body = {
        "new_password": "newtestpassword",
        "old_password": "wrongtestpassword"
        }
        request = ApiMethods.change_password(token, body)
        print(request.text)
        Assertions.check_status_code(request, 412)
        Assertions.check_json_field(request, "message")
        Assertions.check_json_field_value(request, "message", "Wrong username or password.")
        reset_password()

    @allure.feature("Тест изменения пароля с валидными данными")
    @allure.description("Тест изменения пароля c одинаковым старым и новым паролем")
    # @pytest.mark.run(order=2)
    def test_change_same_password(self):
        body = {
        "new_password": "testpassword",
        "old_password": "testpassword"
        }
        request = ApiMethods.change_password(token, body)
        print(request.text)
        Assertions.check_status_code(request, 400)


