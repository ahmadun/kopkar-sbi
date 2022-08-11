
from app.model.members import Members,members_schema

from datetime import datetime
from app import response,db
from flask import request, jsonify,abort


def member():
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

def save():
    try:
        nik = request.json.get('nik')
        name = request.json.get('name')
        created_by = request.json.get('created_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        check = Members.query.filter(Members.nik == nik).first()
        if (check is None):
            try:
                data = Members(nik=nik,name=name,created_by=created_by,created_at=now)

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

def update():
    try:
        nik = request.json.get('nik')
        name = request.json.get('name')
    
        updated_by = request.json.get('updated_by')
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    
        data =Members.query.filter_by(nik=nik).first()
        data.name =name
        data.updated_by  = updated_by
        data.updated_at  = now
        db.session.commit()
      
        return response.success(True, 'Sucessfully Change Profile')
    except Exception as e:
        print(e)