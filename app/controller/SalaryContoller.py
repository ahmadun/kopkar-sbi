from datetime import datetime
from marshal import dump


from sqlalchemy import func
from app import response,db
from flask import request, jsonify,abort,json
from app.model.salarys import Salarys,salarys_schema
from app.model.users import Users,users_schema


def index():
    try:
        nik = request.args.get('nik')
        if nik=='':
            data = Salarys.query.join(Users, Salarys.nik==Users.nik).add_columns(Salarys.nik, Users.name, Salarys.basic_salary, Salarys.last_salary, Salarys.last_month_pay)
            result = salarys_schema.dump(data)
            return jsonify(result)
        else:
            data = Salarys.query.join(Users, Salarys.nik==Users.nik) \
            .add_columns(Salarys.nik, Users.name, Salarys.basic_salary, Salarys.last_salary, Salarys.last_month_pay).filter(Salarys.nik==nik)
            result = salarys_schema.dump(data)
            return jsonify(result)

    except Exception as e:
        print(e)

def save():
    try:
        nik = request.json.get('nik')
        basic_salary = request.json.get('basic_salary').replace(',','')
        last_salary = request.json.get('last_salary').replace(',','')
        last_month_pay = request.json.get('last_month_pay')
        created_by = request.json.get('created_by')
        created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        mode = request.json.get('mode')

        print(basic_salary)
        if mode==1:
            data = Salarys.query.filter_by(nik=nik).first()
            data.nik=nik
            data.basic_salary=basic_salary
            data.last_salary=last_salary
            data.last_month_pay=last_month_pay
            data.created_by=created_by
            data.created_at=created_at
            db.session.commit()
            return response.success(True, 'Sucesfully Update Data')         
        else:
            data = Salarys(nik=nik,basic_salary=basic_salary, last_salary=last_salary, last_month_pay=last_month_pay,created_by=created_by,created_at=created_at)
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
             stream.append((i['nik'],i['basic_salary'],i['last_salary'],i['last_month_pay'],i['created_by'],now))
       
        print('insert into salarys (nik,basic_salary,last_salary,last_month_pay,created_by,created_at) VALUES {}'.format(str(stream)[1:-1]))
        db.session.commit()
            

    except Exception as e:
        print(e)