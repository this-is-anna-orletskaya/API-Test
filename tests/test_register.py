import json
import sys
sys.path.append('./lib')
import allure
from api import ApiMethods
from generate import GenerateData
from assertions import Assertions



"""Тестирование регистрации пользователя в системе"""


@allure.epic("Тестирование пользовательской регистрации")
@allure.severity(allure.severity_level.CRITICAL)
class TestRegister():

    def test_register_new_user(self):

        body = {
            
        "email": GenerateData.generate_email(10) + "@gmail.com",
        "password": GenerateData.generate_password(8),
        "username": GenerateData.generate_name(3)

        }
        request = ApiMethods.register_new_user(body)
        Assertions.check_status_code(request, 200)
        Assertions.check_json_fields(request, ("id", "name", "username", "created", "updated"))
        Assertions.check_json_field_value(request, "username", body.get("username"))


    def test_register_not_new_user(self):

        body = {
        
        "email": "testmail@gmail.com",
        "password": "testpassword123",
        "username": "testname"

        }
        try:
            request = ApiMethods.register_new_user(body)
            Assertions.check_status_code(request, 400)
        except AssertionError:
            request = ApiMethods.register_new_user(body)
            Assertions.check_status_code(request, 400)
        finally: 
            Assertions.check_json_fields(request, ("code", "message"))
            Assertions.check_json_field_value(request, "message", "A user with this username already exists.")
        

    def test_register_new_user_short_password(self):

        body = {
        
        "email": GenerateData.generate_email(10) + "@gmail.com",
        "password": GenerateData.generate_password(7),
        "username": GenerateData.generate_name(10)

        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
        # Assertions.check_json_fields(request, ("code", "message"))
        # Assertions.check_json_field_value(request, "message", "No or invalid user register object provided.")


    def test_register_new_user_short_username(self):
        
        body = {
        
        "email": GenerateData.generate_email(8) + "@gmail.com",
        "password": GenerateData.generate_password(8),
        "username": GenerateData.generate_name(2)

        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
    #     Assertions.check_json_fields(request, ("code", "message"))
    #     Assertions.check_json_field_value(request, "message", "No or invalid user register object provided.")


    def test_register_new_user_not_unique_id(self):
            
        body = {
        
        "email": GenerateData.generate_email(8) + "@gmail.com",
        "id": 1,
        "password": GenerateData.generate_password(10),
        "username": GenerateData.generate_name(6)

        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)


    def test_register_new_user_without_email(self):

        body = {
            
        "password": GenerateData.generate_password(10),
        "username": GenerateData.generate_name(10)

        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
        Assertions.check_json_fields(request, ("code", "message"))
        Assertions.check_json_field_value(request, "code", 1004)
        Assertions.check_json_field_value(request, "message", "Please specify a username and a password.")


    def test_register_new_user_without_password(self):

        body = {

        "email": GenerateData.generate_email(8) + "@gmail.com",
        "username": GenerateData.generate_name(10)

        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
        Assertions.check_json_fields(request, ("code", "message"))
        Assertions.check_json_field_value(request, "code", 1004)
        Assertions.check_json_field_value(request, "message", "Please specify a username and a password.")


    def test_register_new_user_without_username(self):

        body = {

        "email": GenerateData.generate_email(8) + "@gmail.com",
        "password": GenerateData.generate_password(10)
        
        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
        Assertions.check_json_fields(request, ("code", "message"))
        Assertions.check_json_field_value(request, "code", 1004)
        Assertions.check_json_field_value(request, "message", "Please specify a username and a password.")


    def test_register_new_user_with_empty_data(self):

        body = {
        
        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)
        Assertions.check_json_fields(request, ("code", "message"))
        Assertions.check_json_field_value(request, "code", 1004)
        Assertions.check_json_field_value(request, "message", "Please specify a username and a password.")


    def test_register_new_user_with_long_email(self):

        body = {
            
        "email": GenerateData.generate_email(241) + "@gmail.com",
        "password": GenerateData.generate_password(8),
        "username": GenerateData.generate_name(10)

        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)


    def test_register_new_user_with_invalid_email(self):
        
        body = {
            
        "email": GenerateData.generate_email(10) + "#gmail,com",
        "password": GenerateData.generate_password(8),
        "username": GenerateData.generate_name(10)

        }
        request = ApiMethods.register_new_user(body)
        print(request.text)
        Assertions.check_status_code(request, 400)







