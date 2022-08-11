from app import db,ma
from datetime import datetime

class Members(db.Model):
    nik = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    created_by = db.Column(db.String(250),nullable=False)
    updated_by = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Members {}>'.format(self.name)


class MembersSchema(ma.Schema):
    class Meta:
        fields = ('nik','name','created_at')
member_schema = MembersSchema()
members_schema = MembersSchema(many=True)