from datetime import datetime
from app import response,db
from flask import request, jsonify,abort,json
from app.model.credit_history import Credit_history,credit_historys_schema
from app.model.users import Users,users_schema


def save():
    try:
        nik = request.json.get('nik')
        start = request.json.get('begins')
        end = request.json.get('lastmonth')
        credit = request.json.get('total_credit')
        credit_type = request.json.get('type')
        remarks = request.json.get('remarks')
        created_by = "Ahmadun"
        created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        try:
            if(credit_type=='PRT'):           
                db.engine.execute('update creditprts set status=1 where nik='+nik+' and month between '+start+' and '+end+'')
            elif(credit_type=='Reguler'):           
                db.engine.execute('update creditregs set status=1 where nik='+nik+' and month between '+start+' and '+end+'')
            elif(credit_type=='Konsumptif'):           
                db.engine.execute('update creditkons set status=1 where nik='+nik+' and month between '+start+' and '+end+'')

            data = Credit_history(nik=nik,start=start,end=end,credit=credit,credit_type=credit_type, remarks=remarks,created_by=created_by,created_at=created_at)
            db.session.add(data)
            db.session.commit()
            return response.success(True, 'Sucesfully Save Data')  
        except Exception as e:
            print(e)
       
            
    except Exception as e:
        print(e)

