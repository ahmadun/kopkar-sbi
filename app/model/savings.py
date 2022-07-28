from app import db,ma
from datetime import datetime

class Savings(db.Model):
    nik = db.Column(db.String(20), primary_key=True)
    period = db.Column(db.String(6),nullable=False)
    date_save = db.Column(db.DateTime,primary_key=True,nullable=False)
    save_mand = db.Column(db.BigInteger,default=0)
    save_main = db.Column(db.BigInteger,default=0)
    save_volu = db.Column(db.BigInteger,primary_key=True,default=0)
    created_by = db.Column(db.String(250))
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Savings {}>'.format(self.name)

  
class SavingsSchema(ma.Schema):
    class Meta:
        fields = ('nik','period','date_save','save_mand','save_main','save_volu','name')
saving_schema = SavingsSchema()
savings_schema = SavingsSchema(many=True)