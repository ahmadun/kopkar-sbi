from datetime import datetime
from app import response,db
from flask import request, jsonify,abort


def save():
    try:
        nik = request.form.get('nik')
        jumlah = request.form.get('jumlah')
        tgl = request.form.get('tgl')
        db.engine.execute("INSERT Kopkarsbi.dbo.BLJ_Kontan VALUES (?,?,?,?,?,?)", (nik, tgl,'NAK',jumlah,nik,None))
        db.session.commit()
        return response.success([], 'Sucessfully Add Data')
    except Exception as e:
        print(e)