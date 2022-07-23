from datetime import datetime
from itertools import chain
from marshal import dump
from app import response,db
from flask import request, jsonify,abort,json


def index():
    try:
        nik = request.form.get('nik')
        data=db.engine.execute("exec spKasbonCheck @nik=?", (nik))
        result=json.dumps([dict(row) for row in data.mappings()])
        return response.success(json.loads(result), 'Sucessfully Add Data')
    except Exception as e:
        print(e)



def savetansaksi():
    try:
        req = request.get_json(force=True, silent=True)
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        stream = []
        total=0
        for i in req:
             stream.append((i['nik'],i['date_bon'],i['form'],i['nota'],i['item'],i['qty'],i['price'],i['user'],now))
             total+=int(i['price'])*int(i['qty'])
       
        old = [stream[0][0],stream[0][1],stream[0][3],total,stream[0][7],now,now]
        db.engine.execute('insert into kopkarsbi_new.dbo.kasbons (nik,date_bon,form,nota,item,qty,price,created_by,created_at) VALUES {}'.format(str(stream)[1:-1]))
        db.engine.execute('insert Kopkarsbi.dbo.All_Kasbon values ({})'.format(str(old)[1:-1]))
        db.session.commit()
                     
        return response.success([], 'Sucessfully Add Data')
    except Exception as e:
        print(e)