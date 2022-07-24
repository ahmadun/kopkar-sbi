from datetime import datetime
from marshal import dump
from sqlalchemy import func
from app import response,db
from flask import request, jsonify,abort,json
from app.model.savings import Savings,savings_schema
from app.model.users import Users,users_schema


def index():
    try:
        nik = request.args.get('nik')
        period = request.args.get('period')
        if nik=='':
            data = Savings.query.join(Users, Savings.nik==Users.nik).add_columns(Savings.nik, Users.name, Savings.date_save, Savings.save_main, Savings.save_mand,Savings.save_volu).filter(Savings.period==period)
            result = savings_schema.dump(data)
            return jsonify(result)
        else:
            data = Savings.query.join(Users, Savings.nik==Users.nik) \
            .add_columns(Savings.nik, Users.name, Savings.date_save, Savings.save_main, Savings.save_mand,Savings.save_volu).filter(Savings.nik==nik,Savings.period==period)
            result = users_schema.dump(data)
            return jsonify(result)

    except Exception as e:
        print(e)


def total_saving(nik):
    try:   
        total = db.session.query(
            func.sum(Savings.save_mand).label("save_mand"),
            func.sum(Savings.save_main).label("save_main"),
            func.sum(Savings.save_volu).label("save_volu")).filter(Savings.nik==nik)

        return total

        
    except Exception as e:
        print(e)


def save():
    try:
        nik = request.json.get('nik')
        period = request.json.get('period')
        date_save = request.json.get('date_save')
        save_volu = request.json.get('save_volu')
        created_by = request.json.get('created_by')
        created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        data = Savings(nik=nik,period=period, date_save=date_save, save_volu=save_volu,created_by=created_by,created_at=created_at)
        db.session.add(data)
        db.session.commit()
        return response.success(True, 'Sucesfully Add Data')


              

    except Exception as e:
        print(e)