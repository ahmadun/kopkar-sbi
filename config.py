import os
import urllib
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))

    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};\
                                   SERVER=AHMADUN;\
                                   DATABASE=kopkar-sbi;\
                                   UID=sa;PWD=ahmadun")
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s&autocommit=true" % params
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    autocommit = True