from app import db,ma
from datetime import datetime

class Salarys(db.Model):
    nik = db.Column(db.String(20), primary_key=True)
    basic_salary = db.Column(db.BigInteger, nullable=False)
    last_salary = db.Column(db.BigInteger)
    last_month_pay = db.Column(db.String(6))
    created_by = db.Column(db.String(250),nullable=False)
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Salarys {}>'.format(self.name)

  
class SalarysSchema(ma.Schema):
    class Meta:
        fields = ('nik','name','basic_salary','last_salary','last_month_pay')
salary_schema = SalarysSchema()
salarys_schema = SalarysSchema(many=True)