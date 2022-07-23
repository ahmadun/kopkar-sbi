from app import db,ma
from datetime import datetime

class Creditkons(db.Model):
    month = db.Column(db.String(6), primary_key=True)
    nik = db.Column(db.String(20), primary_key=True)
    credit_main= db.Column(db.BigInteger, nullable=False)
    credit_interest = db.Column(db.BigInteger,nullable=False)
    credit_total = db.Column(db.BigInteger,nullable=False)
    remarks = db.Column(db.String(200))
    code = db.Column(db.String(3),nullable=False)
    status = db.Column(db.CHAR(1),nullable=False)
    created_by = db.Column(db.String(250),nullable=False)
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Creditkons {}>'.format(self.name)

  
class CreditkonsSchema(ma.Schema):
    class Meta:
        fields = ('month','nik','credit_main','credit_interest','credit_total','remarks','code','status')
creditkon_schema = CreditkonsSchema()
creditkons_schema = CreditkonsSchema(many=True)