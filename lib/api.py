from http_requests import HttpMethods



base_url = "https://try.vikunja.io/api/v1"


"""Методы тестируемой API"""


class ApiMethods():

 #USER 

    @staticmethod
    def register_new_user(body):
        resource = "/register"
        url = base_url + resource
        headers = {'Content-Type': 'application/json'}
        result = HttpMethods.post(url, headers, body)
        return result


    @staticmethod    
    def login_user(body):
        resource = "/login"
        url = base_url + resource 
        headers = {
            'Content-Type': 'application/json'
        }
        result = HttpMethods.post(url, headers, body)
        return result
    

    @staticmethod
    def get_user_info(token):
        resource = "/user"
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.get(url, headers)
        return result

    
    @staticmethod
    def change_password(token, body):
        resource = "/user/password"
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.post(url, headers, body)
        return result
    

    @staticmethod
    def deletion_user(token, body):
        resource = "/user/deletion/request"
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json',    
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.post(url, headers, body)
        return result
    

    @staticmethod
    def confirm_deletion_user(token, body):
        resource = "/user/deletion/confirm"
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.post(url, headers, body)
        return result
    

    @staticmethod
    def cancel_deletion_user(token, body):
        resource = "/user/deletion/cancel"
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.post(url, headers, body)
        return result
    
    


 #PROJECT

    @staticmethod
    def create_new_project(token, body):
        resource = "/projects" 
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.put(url, headers, body)
        return result


    @staticmethod
    def get_one_project(project_id, token):
        resource = "/projects/" + project_id
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.get(url, headers)
        return result

    
    @staticmethod
    def update_project(project_id, token, body):
        resource = "/projects/" + project_id
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.post(url, headers, body)
        return result
    
    @staticmethod
    def delete_project(project_id, token, body):
        resource = "/projects/" + project_id
        url = base_url + resource
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
        result = HttpMethods.delete(url, headers)
        return result


