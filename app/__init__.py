
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import *


app=Flask(__name__,template_folder='template')
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
cors = CORS(app)

app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'ahmadun.jambi@gmail.com'  
app.config['MAIL_PASSWORD'] = 'gvnbhstslioclves'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
mail = Mail(app)  

from app.model import users,salarys,creditregs,creditkons,creditprts,savings,saving_masters,credits,credit_history
from app import routes