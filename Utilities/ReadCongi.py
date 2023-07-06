import configparser

config = configparser.RawConfigParser()

config.read("E:\\pythonProject\\ebayCommerceApp\\Configurations\\config.ini")

class Readconfig():
    @staticmethod
    def getUsername():
        Username = config.get('login data', 'Username')
        return Username

    def getPassword(self):
        Password = config.get('login data', 'Password')
        return Password



