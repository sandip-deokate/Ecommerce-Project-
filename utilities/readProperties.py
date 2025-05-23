import configparser
import os

config =configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\Configurations\\config.ini')

class ReadConfig:


    @staticmethod
    def get_url():
        url=config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def get_email():
        email = config.get('commonInfo','email')
        return  email

    @staticmethod
    def get_password():
        password = config.get('commonInfo','password')
        return password
