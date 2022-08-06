from cgitb import html
from datetime import datetime
from marshal import dump
from flask_mail import *  
from sqlalchemy import func
from app import response,db,mail
from flask import Response, make_response, render_template, request, jsonify,abort,json
from app.model.savings import Savings,savings_schema
import pdfkit




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



def emailsend(nik):
    try:  
        email = request.json.get('email')
        print(email)
        data = Savings.query.filter(Savings.nik == nik)  
        total=total_saving(nik)
        htmls=render_template("saving-pdftemplate.html",list=data,total=total)
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdfdata = pdfkit.from_string(htmls, configuration=config)
        
        msg = Message('DATA TABUNGAN '+nik+'', sender = 'ahmadun.jambi@gmail.com', recipients=[email])  
        msg.html=render_template("saving_emailbody.html",nik=nik)
        msg.attach('List Simpanan '+nik+'.pdf', 'application/pdf', pdfdata)
        mail.send(msg)    
        return response.success(True, 'Sucesfully Add Data')
    except Exception as e:
        print(e)


  





        

