from app import db,ma
from datetime import datetime

class Creditprts(db.Model):
    month = db.Column(db.String(6), primary_key=True)
    nik = db.Column(db.String(20), primary_key=True)
    credit= db.Column(db.BigInteger, nullable=False)
    remarks = db.Column(db.String(200))
    status = db.Column(db.CHAR(1),nullable=False)
    created_by = db.Column(db.String(250),nullable=False)
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Creditprts {}>'.format(self.name)

  
class CreditprtsSchema(ma.Schema):
    class Meta:
        fields = ('month','nik','credit','remarks','status')
creditprt_schema = CreditprtsSchema()
creditprts_schema = CreditprtsSchema(many=True)