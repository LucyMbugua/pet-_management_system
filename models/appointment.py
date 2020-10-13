from main import db
from sqlalchemy import func

class AppointmentModel(db.Model):
    __tablename__="appointments"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    time = db.Column(db.DateTime(timezone=True))
    member_id =db.Column(db.Integer, db.ForeignKey('members.id'))
    pet_id =db.Column(db.Integer, db.ForeignKey('pets.id'))
    doctor_id =db.Column(db.Integer, db.ForeignKey('doctors.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    members = db.relationship('MemberModel', backref="appointment", lazy=True)
    pets = db.relationship('PetModel', backref="appointment", lazy=True)
    doctors = db.relationship('DoctorModel', backref="appointment", lazy=True)
    
    def create_record(self):
        db.session.add(self)
        db.session.commit()
    #fetch records
    @classmethod
    def fetch_all(cls):
        return cls.query.all()
    