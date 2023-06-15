import json
from bs4 import BeautifulSoup
from jsonschema import validate


class Assertions():

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print(f"Статус код: {str(result.status_code)}")
    
    @staticmethod
    def check_json_field(result, value):
        field = json.loads(result.text)
        if value in field:
            print(f'Полe "{value}" присутствует')
    
    @staticmethod
    def check_json_fields(result, values):
        value_list = list(values)
        for i in value_list:
            Assertions.check_json_field(result, i)
    
    @staticmethod
    def check_json_field_value(result, name, value):
        field = json.loads(result.text)
        result_field = field[name]  
        assert result_field == value
        print(f'Значение поля "{name}" верно')

    @staticmethod
    def check_html_tag_value(result, tag_name, value):
        html_response = result.text 
        soup = BeautifulSoup(html_response, features="html.parser")
        tag = soup.find(tag_name)
        title = tag.text
        assert title == value
        print(f'Значение тэга "{tag_name}" верно')
    
    @staticmethod
    def check_validate_response_json_schema(response):
        with open('lib\schema.json') as file:
            string = file.read()
            schema = json.loads(string)
        response_json = json.loads(response.text)
        validate(response_json, schema)
        print("Валидация по JSON SCHEMA успешна")
