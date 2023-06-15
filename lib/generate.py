import random



class GenerateData():

    @staticmethod
    def generate_email(length):
        email = ''
        for i in range(length):
            email = email + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnm_'))
        return email
    
    @staticmethod 
    def generate_password(length):
        password = ''
        for i in range(length):
            password = password + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()—_+=;:,./?\|`~[]{}'))
        return password 
    
    @staticmethod
    def generate_name(length):
        username = ''
        for i in range(length):
            username = username + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_'))
        return username
    
    