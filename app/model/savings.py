from app import db,ma
from datetime import datetime

class Savings(db.Model):
    nik = db.Column(db.String(20), primary_key=True)
    date_save = db.Column(db.DateTime, nullable=False)
    save_mand = db.Column(db.BigInteger)
    save_main = db.Column(db.BigInteger)
    save_volu = db.Column(db.BigInteger)
    created_by = db.Column(db.String(250))
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Savings {}>'.format(self.name)

  
class SavingsSchema(ma.Schema):
    class Meta:
        fields = ('nik','date_save','save_mand','save_main','save_volu')
saving_schema = SavingsSchema()
savings_schema = SavingsSchema(many=True)