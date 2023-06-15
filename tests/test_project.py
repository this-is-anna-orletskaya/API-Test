import sys
sys.path.append('./lib')
import allure
from api import ApiMethods
from assertions import Assertions
from generate import GenerateData



"""Тестирование функциональности работы с проектом"""


@allure.epic("Тестирование функциональности работы с проектом")
@allure.severity(allure.severity_level.NORMAL)
class TestProject():

    @allure.feature("Создание нового проекта")
    def test_create_new_project(self, set_for_project):
        global token
        token = set_for_project

        body ={
        
        "background_blur_hash": "LKN]Rv%2Tw=w]~RBVZRi};RPxuwH",
        "description": "New test project",
        "hex_color": "556B2F",
        "identifier": GenerateData.generate_name(8),
        "is_archived": False,
        "is_favorite": False,
        "position": 0,
        "title": "New test project"
        }
        request = ApiMethods.create_new_project(token, body)
        print(request.text)
        Assertions.check_status_code(request, 201)
        request_json = request.json()
        global project_id
        project_id = request_json.get("id")
        Assertions.check_validate_response_json_schema(request)
        
        
    @allure.feature("Получение информации о проекте")
    def test_get_project(self):   

        request = ApiMethods.get_one_project(str(project_id), token)

        print(request.text)

        Assertions.check_status_code(request, 200)
        Assertions.check_validate_response_json_schema(request)


    @allure.feature("Внесение изменений в проект")
    def test_update_project(self):

        body = {
        "description": "Test project description",
        "title": "New test project"
        }
        request = ApiMethods.update_project(str(project_id), token, body)

        print(request.text)

        Assertions.check_status_code(request, 200)
        Assertions.check_validate_response_json_schema(request)


    @allure.feature("Удаление проекта")
    def test_delete_project(self):

        body = {}

        request = ApiMethods.delete_project(str(project_id), token, body)

        print(request.text)

        Assertions.check_status_code(request, 200)
        Assertions.check_json_field_value(request, "message", "Successfully deleted.")

