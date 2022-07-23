from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from sqlalchemy import true
from app.model.users import Users,users_schema

from datetime import datetime
from app import response,db
from flask import request, jsonify,abort
from flask_jwt_extended import *

from datetime import timedelta


def checkanggota(id):
    try:
        data = Users.query.filter_by(id=id).first()
        result = users_schema.dump(data)
        return jsonify(result)

    except Exception as e:
        print(e)

def save():
    try:
        nik = request.form.get('nik')
        name = request.form.get('name')
        no_hp = request.form.get('no_hp')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        created_by = request.form.get('created_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


        data = Users(nik=nik,name=name,role=role,no_hp=no_hp,email=email,created_by=created_by,created_at=now)
        data.setPassword(password)
        db.session.add(data)
        db.session.commit()

        return response.success([], 'Sucessfully Add Data')
    except Exception as e:
        print(e)


def changepwd():
    try:
        nik = request.form.get('nik')
        password = request.form.get('password')
        updated_by = request.form.get('created_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        data =Users.query.filter_by(nik=nik).first()
        data.password = password
        data.updated_by  = updated_by
        data.updated_at  = now
        db.session.commit()
      

        return response.success([], 'Sucessfully Change Password')
    except Exception as e:
        print(e)

def updateuserinfo():
    try:
        nik = request.form.get('nik')
        no_hp = request.form.get('no_hp')
        role = request.form.get('role')
        email = request.form.get('email')
        updated_by = request.form.get('updated_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        data =Users.query.filter_by(nik=nik).first()
        data.no_hp = no_hp
        data.role = role
        data.email = email
        data.updated_by  = updated_by
        data.updated_at  = now
        db.session.commit()
      

        return response.success([], 'Sucessfully Update User')
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
            return response.badRequest([], 'Password is wrong!')

    
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

