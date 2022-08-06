from app import db,ma
from datetime import datetime

class Credit_history(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nik = db.Column(db.String(20))
    start= db.Column(db.String(6),nullable=False)
    end = db.Column(db.String(6),nullable=False)
    credit = db.Column(db.BigInteger,nullable=False)
    credit_type = db.Column(db.String(10))
    remarks = db.Column(db.String(250))
    created_by = db.Column(db.String(50),nullable=False)
    updated_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Credit_history {}>'.format(self.nik)

  
class Credit_historySchema(ma.Schema):
    class Meta:
        fields = ('id','nik','start','end','credit','credit_type','remarks','remarks')
credit_history_schema = Credit_historySchema()
credit_historys_schema = Credit_historySchema(many=True)