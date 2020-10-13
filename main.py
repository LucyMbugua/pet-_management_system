from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
#import config class
from settings.configs import DevelopmentConfig, ProductionConfig
# import db connection
from settings.db_connect import conn

app = Flask(__name__)
#tell flask which config settings to use
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

#import models
from models.member import MemberModel
from models.doctor import DoctorModel
from models.pet import PetModel
from models.appointment import AppointmentModel

@app.before_first_request
def create_tables():
    db.create_all()
    #db.drop_all()
 


@app.route('/members', methods=['GET','POST'])
def members():

    members=MemberModel.fetch_all()
    print(members)
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        
        record = MemberModel(fname=fname,lname=lname,email=email)
        record.create_record()
        flash("Record has been successifully created","success")
       
        return redirect(url_for('members'))

    return render_template('members.html', all_members = members)
   

@app.route("/add_pet/<member_id>", methods=['GET','POST'])
def add_pet(member_id):
    
    if request.method == 'POST':
        pet_type= request.form['pet_type']
        pet_name= request.form['pet_name']
        new_pet = PetModel(member_id=member_id, pet_name=pet_name, pet_type=pet_type)
        new_pet.create_record()
        
        flash("Pet added successifully","success")
        return redirect(url_for('members'))

@app.route('/about')
def about():
    return render_template('contact.html')

@app.route('/contact-us')
def contact():
    return render_template('about.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/appointments')
def appointments():
    return render_template('index.html')

@app.route('/doctors')
def doctors():
    return render_template('index.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/delete/<member_id>', methods=['POST'])
def delete_member(member_id):
    record =MemberModel.query.filter_by(id=member_id).first()
    if record:
        db.session.delete(record)
        db.session.commit()
        flash("Successifully deleted","warning")
        
    else:
        flash("Error!! Operation unsuccessiful", "warning")

    return redirect(url_for('members'))

