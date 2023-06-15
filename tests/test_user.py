import sys
sys.path.append('./lib')
import allure
from api import ApiMethods
from assertions import Assertions



"""Тестирование пользовательской функциональности"""


@allure.epic("Тестирование пользовательской функциональности")
@allure.feature("Тестирование получения информации о пользователе", "Тестирование удаления пользователя")
@allure.severity(allure.severity_level.NORMAL)
class TestUser():

    @allure.story("Тест получения информации о пользователе с валидными данными")
    def test_get_user_info(self, set_for_user):
        global token
        token = set_for_user
        request = ApiMethods.get_user_info(token)
        print(request.text)
        Assertions.check_status_code(request, 200)
    
    @allure.story("Тест получения информации о пользователе с невалидными данными")
    @allure.description("Используется несуществующий токен")
    def test_get_user_info_invalid_token(self):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.SflKxwRJSMeKKF2QT"
        request = ApiMethods.get_user_info(token)
        print(request.text)
        Assertions.check_status_code(request, 401)


    @allure.story("Тест полного пути удаления пользователя")
    @allure.description("Тестирование запроса на удаление с последующим подтверждением и отменой удаления")
    def test_delete_user_all_path(self):
        
        body_req = {
        "password": "testpassword"
        }
        with allure.step("Запрос на удаление пользователя с паролем в теле запроса"):
            request = ApiMethods.deletion_user(token, body_req)
            print(request.text)
            Assertions.check_status_code(request, 200)
            Assertions.check_json_field_value(request, "message", "Successfully requested deletion.")
        
        body_conf = {
        "token": token
        }
        with allure.step("Подтверждение удаления пользователя"):
            request_conf = ApiMethods.confirm_deletion_user(token, body_conf)
            print(request.text)
            Assertions.check_status_code(request_conf, 204)
            

        body_canс = {
        "password": "testpassword"
        }
        with allure.step("Отмена удаления пользователя"):
            request_canc = ApiMethods.cancel_deletion_user(token, body_canс)
            print(request.text)
            Assertions.check_status_code(request, 200)

    @allure.story("Тест удаления пользователя с невалидными данными")
    @allure.description("Используется неверный пароль")
    def test_delete_user_wrong_password(self):
    
        body_req = {
        "password": "wrongpassword"
        }
        request = ApiMethods.deletion_user(token, body_req)
        print(request.text)
        Assertions.check_status_code(request, 412)
        Assertions.check_json_fields(request, ("code", "message"))



        

