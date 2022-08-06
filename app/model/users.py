from app import db,ma
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    nik = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    no_hp = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250),primary_key=True)
    email_verified_at = db.Column(db.DateTime)
    password = db.Column(db.String(250),nullable=False)
    role = db.Column(db.BigInteger, nullable=False)
    created_by = db.Column(db.String(250),nullable=False)
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Users {}>'.format(self.name)

    def setPassword(self,password):
        self.password = generate_password_hash(password)
    
    def checkPassword(self,password):
        return check_password_hash(self.password, password)


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('nik','name','no_hp','email','role','email_verified_at')
user_schema = UsersSchema()
users_schema = UsersSchema(many=True)