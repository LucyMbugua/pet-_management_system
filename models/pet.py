from main import db
from sqlalchemy import func

class PetModel(db.Model):
    __tablename__="pets"
    id = db.Column(db.Integer, primary_key=True)
    member_id =db.Column(db.Integer, db.ForeignKey('members.id'))
    pet_type = db.Column(db.String(55), nullable=False,unique=True)
    pet_name = db.Column(db.String(55), nullable=False,unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    def create_record(self):
        db.session.add(self)
        db.session.commit()
    