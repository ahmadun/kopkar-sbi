from datetime import datetime
from marshal import dump

from sqlalchemy import func
from app import response,db
from flask import request, jsonify,abort,json
from app.model.savings import Savings,savings_schema




def index(nik):
    try:
        data = Savings.query.filter(Savings.nik == nik)
        list= savings_schema.dump(data)      
        total= savings_schema.dump(total_saving(nik))
        response = {'data':list, 'total':total}
        return jsonify(response)
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