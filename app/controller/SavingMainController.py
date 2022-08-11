from datetime import datetime
from marshal import dump
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from app import response,db
from flask import request, jsonify,abort,json
from app.model.savings import Savings,savings_schema
from app.model.members import Members,members_schema


def index():
    try:
        nik = request.args.get('nik')
        period = request.args.get('period')
        if nik=='':
            data = Savings.query.join(Members, Savings.nik==Members.nik).add_columns(Savings.nik, Members.name, Savings.date_save, Savings.save_main, Savings.save_mand,Savings.save_volu).filter(Savings.period==period)
            result = savings_schema.dump(data)
            return jsonify(result)
        else:
            data = Savings.query.join(Members, Savings.nik==Members.nik).add_columns(Savings.nik, Members.name, Savings.date_save, Savings.save_main, Savings.save_mand,Savings.save_volu).filter(Savings.nik==nik,Savings.period==period)
            result = savings_schema.dump(data)
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

def update():
    try:
        nik = request.json.get('nik')
        save_volu = request.json.get('save_volu')
        save_main = request.json.get('save_main')
        save_mand = request.json.get('save_mand')
        created_by = request.json.get('created_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        data =Savings.query.filter_by(nik=nik).first()
        data.save_volu =save_volu
        data.save_main =save_main
        data.save_mand =save_mand
        data.updated_by  = created_by
        data.updated_at  = now
        db.session.commit()

       
        return response.success(True, 'Sucesfully Add Data')


    except Exception as e:
        print(e)


def upload():
    try:       
        req = request.get_json(force=True, silent=True)
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        stream = []
        for i in req:
             stream.append((i['nik'],i['period'],i['date_save'],i['save_mand'],i['save_main'],i['save_volu'],'220021',now))      
        db.engine.execute('insert into savings (nik,period,date_save,save_mand,save_main,save_volu,created_by,created_at) VALUES {}'.format(str(stream)[1:-1]))
        db.session.commit()
        return response.success(True, 'Sucesfully Add Data')
    except Exception as e:
        print(e)


def createsaving():
    try:
        created_by = request.json.get('created_by')
        month = request.json.get('month')
  
        db.session.execute("CALL spCreateSaving("+month+", "+created_by+")")   
        db.session.commit()
        return response.success(True, 'Sucessfully Create Data')
    except Exception as e:
        print(e)