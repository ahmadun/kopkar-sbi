from app import db,ma
from datetime import datetime

class Credits(db.Model):
    id = db.Column(db.CHAR(3), primary_key=True)
    desc= db.Column(db.String(250), nullable=False)
    interest = db.Column(db.Numeric(2,2),nullable=False)
    created_by = db.Column(db.String(250),nullable=False)
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Credits {}>'.format(self.name)

  
class CreditsSchema(ma.Schema):
    class Meta:
        fields = ('id','desc','interest')
credit_schema = CreditsSchema()
credits_schema = CreditsSchema(many=True)