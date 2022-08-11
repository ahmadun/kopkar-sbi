from sqlalchemy import true
from app.model.users import Users,users_schema
from app.model.members import Members,members_schema

from datetime import datetime
from app import response,db
from flask import request, jsonify,abort
from flask_jwt_extended import *
from werkzeug.security import generate_password_hash

from datetime import timedelta


def checkmember():
    try:
        nik = request.args.get('nik')
        if (nik!=""):
            data = Members.query.filter(Members.nik==nik)       
            result = members_schema.dump(data)
            return jsonify(result)
        else:
            data = Members.query.all()      
            result = members_schema.dump(data)
            return jsonify(result)


    except Exception as e:
        print(e)

        

def checkuser():
    try:
        nik = request.args.get('nik')
        if (nik!=""):
            data = Users.query.filter(Users.nik==nik)       
            result = users_schema.dump(data)
            return jsonify(result)
        else:
            data = Users.query.all()      
            result = users_schema.dump(data)
            return jsonify(result)


    except Exception as e:
        print(e)

def save():
    try:
        nik = request.json.get('nik')
        name = request.json.get('name')
        no_hp = request.json.get('no_hp')
        email = request.json.get('email')
        password = request.json.get('password')
        role = request.json.get('role')
        created_by = request.json.get('created_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        check = Users.query.filter(Users.nik == nik).first()
        if (check is None):
            try:
                data = Users(nik=nik,name=name,role=role,no_hp=no_hp,email=email,created_by=created_by,created_at=now)
                data.setPassword(password)
                db.session.add(data)
                db.session.commit()
                return response.success(True, 'Sucessfully Add Data')
            except Exception as e:
                print(e)
        else:
            return response.success(False, 'Data is Exist')


        

        return response.success(True, 'Sucessfully Add Data')
    except Exception as e:
        print(e)


def changepwd():
    try:
        nik = request.json.get('nik')
        password = request.json.get('password')
        updated_by = request.json.get('created_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        data =Users.query.filter_by(nik=nik).first()
        data.password=generate_password_hash(password)
        data.updated_by  = updated_by
        data.updated_at  = now
        db.session.commit()
      
        return response.success(True, 'Sucessfully Change Password')
    except Exception as e:
        print(e)

def chagenpwduser():
    try:
        nik = request.json.get('nik')
        password = request.json.get('password')
        passwordold = request.json.get('passwordold')
        updated_by = request.json.get('created_by')   
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        user = Users.query.filter_by(nik=nik).first()
        if not user.checkPassword(passwordold):
            return response.success(False, 'Password Lama Salah')


        data =Users.query.filter_by(nik=nik).first()
        data.password=generate_password_hash(password)
        data.updated_by  = updated_by
        data.updated_at  = now
        db.session.commit()
        return response.success(True, 'Sucessfully Change Password')
            

    except Exception as e:
        print(e)

def updateuserinfo():
    try:
        nik = request.json.get('nik')
        name = request.json.get('name')
        no_hp = request.json.get('no_hp')
        role = request.json.get('role')
        email = request.json.get('email')
        updated_by = request.json.get('updated_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

      

        data =Users.query.filter_by(nik=nik).first()
        data.name =name
        data.no_hp = no_hp
        data.role = role
        data.email = email
        data.updated_by  = updated_by
        data.updated_at  = now
        db.session.commit()
      
        return response.success(True, 'Sucessfully Change Profile')
    except Exception as e:
        print(e)


def usersapprove():
    try:
        nik = request.json.get('nik')
        updated_by = request.json.get('updated_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        approve = request.json.get('approve')

        data =Users.query.filter_by(nik=nik).first()
        if(approve==True):
            data.updated_by  = updated_by
            data.email_verified_at  = now
            data.updated_at  = now
        else:
            data.updated_by  = updated_by
            data.email_verified_at  = None
            data.updated_at  = now
   
        
        db.session.commit()
      
        return response.success(True, 'Sucessfully Change Profile')
    except Exception as e:
        print(e)

def singleObject(data):
    data = {
        'nik' : data.nik,
        'name': data.name,
        'email' : data.email,
        'role' : data.role
    }

    return data

def login():
    try:
        nik = request.json.get('nik')
        password = request.json.get('password')

        user = Users.query.filter_by(nik=nik).first()

        if not user:
            return response.badRequest([], 'User Not Registered')
        
        if not user.checkPassword(password):
             return response.success({
                "isAuthenticated":"false"
            },"Login Failed")

    
        data = singleObject(user)
        expires =timedelta(days=7)
        expires_refresh = timedelta(days=7)

        acces_token = create_access_token(data, fresh=True, expires_delta= expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
            "isAuthenticated":"true",
            'nik':user.nik,
            'name':user.name,
            'role':user.role,
            "email" : user.email,
            "token" : acces_token,
        },"Login Success")
        
    except Exception as e:
        print(e)

