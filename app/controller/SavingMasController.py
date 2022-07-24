from datetime import datetime
from marshal import dump


from sqlalchemy import func
from app import response,db
from flask import request, jsonify,abort,json
from app.model.saving_masters import Savings_masters,savings_masters_schema
from app.model.users import Users,users_schema


def index():
    try:
        nik = request.args.get('nik')
        if nik=='':
            data = Savings_masters.query.join(Users, Savings_masters.nik==Users.nik).add_columns(Savings_masters.nik, Users.name, Savings_masters.save_main, Savings_masters.save_mand, Savings_masters.save_volu,Savings_masters.updated_at)
            result = savings_masters_schema.dump(data)
            return jsonify(result)
        else:
            data = Savings_masters.query.join(Users, Savings_masters.nik==Users.nik) \
            .add_columns(Savings_masters.nik, Users.name, Savings_masters.save_main, Savings_masters.save_mand, Savings_masters.save_volu,Savings_masters.updated_at).filter(Savings_masters.nik==nik)
            result = savings_masters_schema.dump(data)
            return jsonify(result)

    except Exception as e:
        print(e)

def save():
    try:
        nik = request.json.get('nik')
        save_main = request.json.get('save_main')
        save_mand = request.json.get('save_mand')
        save_volu = request.json.get('save_volu')
        created_by = request.json.get('created_by')
        created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        mode = request.json.get('mode')

        if mode==1:
            data = Savings_masters.query.filter_by(nik=nik).first()
            data.nik=nik
            data.save_main=save_main
            data.save_mand=save_mand
            data.save_volu=save_volu
            data.created_by=created_by
            data.created_at=created_at
            db.session.commit()
            return response.success(True, 'Sucesfully Update Data')         
        else:
            data = Savings_masters(nik=nik,save_main=save_main, save_mand=save_mand, save_volu=save_volu,created_by=created_by,created_at=created_at)
            db.session.add(data)
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
             stream.append((i['nik'],i['save_main'],i['save_mand'],i['save_volu'],i['created_by'],now))
       
        print('insert into savings_masters (nik,save_main,save_mand,save_volu,created_by,created_at) VALUES {}'.format(str(stream)[1:-1]))
        db.session.commit()
            

    except Exception as e:
        print(e)