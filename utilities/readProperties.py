import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():  # access this method directly using class name use decorator (self removed) # without creating object
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUserEmail():
        username = config.get("common info", "emailAdd")
        return username

    @staticmethod
    def getUserPassword():
        password = config.get("common info", "password")
        return password
