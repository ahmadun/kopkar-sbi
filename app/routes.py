from flask_cors import cross_origin
from app import app,response
from app.controller import UserContoller,CashContoller,BonContoller,CreditController,SalaryContoller,SavingContoller,SavingMasController,SavingMainController,CreditHisController,MemberContoller
from flask import render_template, request
from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import unset_jwt_cookies

@app.route('/')
def index():
    return 'Hello World'

@app.route('/api/users', methods=['GET', 'POST','PUT'])
def users():
    if request.method == 'PUT':
        return UserContoller.updateuserinfo()
    else:
        return UserContoller.save()

@app.route('/api/usersapprove', methods=['PUT'])
def usersapprove():
    if request.method == 'PUT':
        return UserContoller.usersapprove()



@app.route('/api/users/pwd', methods=['PUT'])
def pwd():
    if request.method == 'PUT':
        return UserContoller.changepwd()
    else:
        return UserContoller.save()

@app.route('/api/users/chagenpwduser', methods=['POST'])
def chagenpwduser():
    if request.method == 'POST':
        return UserContoller.chagenpwduser()

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return UserContoller.login()

@app.route('/api/checkmember', methods=['GET'])
def checkmember():
    if request.method == 'GET':
        return UserContoller.checkmember()

@app.route('/api/checkuser', methods=['GET'])
def checkuser():
    if request.method == 'GET':
        return UserContoller.checkuser()

@app.route("/api/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@app.route("/api/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'Sukses')

@app.route('/api/changepwd', methods=['PUT'])
def changepwd():
    if request.method == 'PUT':
        return UserContoller.changepwd()

@app.route('/api/saveblgkontan', methods=['POST'])
def savetrans():
    if request.method == 'POST':
        return CashContoller.save()

@app.route('/api/checkkasbon', methods=['GET'])
def checkkasbon():
    if request.method == 'GET':
        return BonContoller.index()


@app.route('/api/savetrans', methods=['POST'])
def savecashbon():
    if request.method == 'POST':
        return BonContoller.savetansaksi()

@app.route('/api/processcredit', methods=['POST'])
def processcredit():
    if request.method == 'POST':
        code = request.args.get('code')
        return CreditController.processcredit(code)

@app.route('/api/detail_credit', methods=['GET'])
def detail_credit():
    if request.method == 'GET':
        return CreditController.detail_credit()



@app.route('/api/credit_list/<nik>', methods=['GET'])
def list_credit(nik):
    if request.method == 'GET':
        return CreditController.index(nik)


@app.route('/api/salarys', methods=['GET','POST'])
def salarys():
    if request.method == 'GET':
        return SalaryContoller.index()
    elif request.method == 'POST':
        return SalaryContoller.save()

@app.route('/api/uploadsalary', methods=['POST'])
def uploadsalary():
    if request.method == 'POST':
        return SalaryContoller.upload()

@app.route('/api/savingmaster', methods=['GET','POST'])
def savingmaster():
    if request.method == 'GET':
        return SavingMasController.index()
    elif request.method == 'POST':
        return SavingMasController.save()

@app.route('/api/uploadsavingmaster', methods=['POST'])
def uploadsavingmaster():
    if request.method == 'POST':
        return SavingMasController.upload()

@app.route('/api/saving/<nik>', methods=['GET'])
def saving(nik):
    if request.method == 'GET':
        return SavingContoller.index(nik)

@app.route('/api/savingmain', methods=['GET','POST','PUT'])
def savingmain():
    if request.method == 'GET':
        return SavingMainController.index()
    if request.method == 'POST':
        return SavingMainController.save()
    if request.method == 'PUT':
        return SavingMainController.update()

@app.route('/api/savemainupload', methods=['POST'])
def savemainup():
    if request.method == 'POST':
        return SavingMainController.upload()

@app.route('/api/createsaving', methods=['POST'])
def createsaving():
    if request.method == 'POST':
        return SavingMainController.createsaving()

@app.route('/api/creditsmst', methods=['GET'])
def creditsmst():
    if request.method == 'GET':
        return CreditController.creditsmst()


@app.route('/api/updatecredit', methods=['PUT'])
def updatecredit():
    if request.method == 'PUT':
        return CreditController.updatecredit()


@app.route('/api/sendsaving/<nik>',methods=['POST'])  
def sendsaving(nik):  
    if request.method == 'POST':
        return SavingContoller.emailsend(nik)

@app.route('/api/listcreditall',methods=['GET'])  
def listcreditall():  
    if request.method == 'GET':
        return CreditController.listcreditall()

@app.route('/api/credithistory',methods=['POST'])  
def credithistory():  
    if request.method == 'POST':
        return CreditHisController.save()


@app.route('/api/member', methods=['GET','POST','PUT'])
def member():
    if request.method == 'GET':
        return MemberContoller.member()
    elif request.method == 'POST':
        return MemberContoller.save()
    elif request.method == 'PUT':
        return MemberContoller.update()