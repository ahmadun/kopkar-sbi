# import os
# import urllib
# basedir = os.path.abspath(os.path.dirname(__file__))

# class Config(object):
#     HOST = str(os.environ.get("DB_HOST"))
#     DATABASE = str(os.environ.get("DB_DATABASE"))
#     USERNAME = str(os.environ.get("DB_USERNAME"))
#     PASSWORD = str(os.environ.get("DB_PASSWORD"))

#     JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
#     params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};\
#                                    SERVER=AHMADUN;\
#                                    DATABASE=kopkar-sbi;\
#                                    UID=sa;PWD=ahmadun")
#     SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s&autocommit=true" % params
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_RECORD_QUERIES = True
#     autocommit = True

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # HOST = '127.0.0.1:3307'
    HOST = '156.67.219.145:3306'
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    # DATABASE = 'kopkarsbi'
    # USERNAME ='root'
    # PASSWORD ='ahmadun'

    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


