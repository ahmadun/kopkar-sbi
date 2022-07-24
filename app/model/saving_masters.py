from app import db,ma
from datetime import datetime

class Savings_masters(db.Model):
    nik = db.Column(db.String(20), primary_key=True)
    save_mand = db.Column(db.BigInteger)
    save_main = db.Column(db.BigInteger)
    save_volu = db.Column(db.BigInteger)
    created_by = db.Column(db.String(250))
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Savings_masters {}>'.format(self.name)

  
class Savings_mastersSchema(ma.Schema):
    class Meta:
        fields = ('nik','save_mand','save_main','save_volu','updated_at','name')
savings_master_schema = Savings_mastersSchema()
savings_masters_schema = Savings_mastersSchema(many=True)