from datetime import datetime
from marshal import dump

from sqlalchemy import func
from app import response,db
from flask import request, jsonify,abort,json
from app.model.creditregs import Creditregs,creditregs_schema
from app.model.creditkons import Creditkons,creditkons_schema
from app.model.creditprts import Creditprts,creditprts_schema
from app.model.credits import Credits,credits_schema


def index(nik):
    try:
        data=db.engine.execute("exec spListCredit @nik=?", (nik))
        result=json.dumps([dict(row) for row in data.mappings()])
        return response.success(json.loads(result), 'Sucessfully Add Data')
    except Exception as e:
        print(e)

def detail_credit():
    try:
        nik = request.args.get('nik')
        code = request.args.get('code')
        if code=='REG':  
            data = Creditregs.query.filter(Creditregs.nik == nik,Creditregs.status == 0)
            list= creditregs_schema.dump(data)      
            total= creditregs_schema.dump(pinjaman_reg_total(nik))
            response = {'data':list, 'total':total}
            return jsonify(response)
        elif code=='KON':
            data = Creditkons.query.filter(Creditkons.nik == nik,Creditkons.status == 0)
            list= creditkons_schema.dump(data)      
            total= creditkons_schema.dump(pinjaman_kons_total(nik))
            response = {'data':list, 'total':total}
            return jsonify(response)
        elif code=='PRT':
            data = Creditprts.query.filter(Creditprts.nik == nik,Creditprts.status == 0)
            list= creditprts_schema.dump(data)      
            total= creditprts_schema.dump(pinjaman_prt_total(nik))
            response = {'data':list, 'total':total}
            return jsonify(response)
   
    except Exception as e:
        print(e)


def pinjaman_reg_total(nik):
    try:
        
        total = db.session.query(
            func.count(Creditregs.month).label("month"),
            func.sum(Creditregs.credit_main).label("credit_main"),
            func.sum(Creditregs.credit_interest).label("credit_interest"),
            func.sum(Creditregs.credit_interest).label("credit_total")).filter(Creditregs.nik == nik,Creditregs.status == 0)

        return total

        
    except Exception as e:
        print(e)

def pinjaman_kons_total(nik):
    try:      
        total = db.session.query(
            func.count(Creditkons.month).label("month"),
            func.sum(Creditkons.credit_main).label("credit_main"),
            func.sum(Creditkons.credit_interest).label("credit_interest"),
            func.sum(Creditkons.credit_interest).label("credit_total")).filter(Creditkons.nik == nik,Creditkons.status == 0)

        return total

        
    except Exception as e:
        print(e)


def pinjaman_prt_total(nik):
    try:      
        total = db.session.query(
            func.count(Creditprts.month).label("month"),
            func.sum(Creditprts.credit).label("credit")).filter(Creditprts.nik == nik,Creditprts.status == 0)

        return total

        
    except Exception as e:
        print(e)



def processcredit(code):
    try:      
        if(code=='reg'):
            creditreg(request.get_json(force=True, silent=True))
            return response.success(True, 'Sucesfully Add Data')
        elif(code=='kon'):
            creditkons(request.get_json(force=True, silent=True))
            return response.success(True, 'Sucesfully Add Data')
        elif(code=='prt'):
            creditprt(request.get_json(force=True, silent=True))
            return response.success(True, 'Sucesfully Add Data')
      
    except Exception as e:
        print(e)


def creditreg(req):
    try:       
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        stream = []
        for i in req:
             stream.append((i['month'],i['nik'],i['mand'].replace("Rp", "").replace(",",""),i['interest'].replace("Rp", "").replace(",",""),i['total'].replace("Rp", "").replace(",",""),i['remarks'],'220021',now,0))      
        db.engine.execute('insert into creditregs (month,nik,credit_main,credit_interest,credit_total,remarks,created_by,created_at,status) VALUES {}'.format(str(stream)[1:-1]))
        db.session.commit()
       
    except Exception as e:
        print(e)

def creditkons(req):
    try:       
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        stream = []
        for i in req:
             stream.append((i['month'],i['nik'],i['mand'].replace("Rp", "").replace(",",""),i['interest'].replace("Rp", "").replace(",",""),i['total'].replace("Rp", "").replace(",",""),i['remarks'],i['code'],'220021',now,0))      
        db.engine.execute('insert into creditkons (month,nik,credit_main,credit_interest,credit_total,remarks,code,created_by,created_at,status) VALUES {}'.format(str(stream)[1:-1]))
        db.session.commit()
        return response.success(True, 'Sucesfully Add Data')
    except Exception as e:
        print(e)

def creditprt(req):
    try:       
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        stream = []
        for i in req:
             stream.append((i['month'],i['nik'],i['mand'].replace("Rp", "").replace(",",""),i['remarks'],'220021',now,0))      
        db.engine.execute('insert into creditprts (month,nik,credit,remarks,created_by,created_at,status) VALUES {}'.format(str(stream)[1:-1]))
        db.session.commit()
        return response.success(True, 'Sucesfully Add Data')
    except Exception as e:
        print(e)


def creditsmst():
    try:
        data = Credits.query.all();    
        result= credits_schema.dump(data)      
        return jsonify(result)
    except Exception as e:
        print(e)


