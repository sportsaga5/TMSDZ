import os
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5Q0VmhsgUv8HL4CzfVhM'

db = SQLAlchemy(app)

guests = db.Table(
    'event_guests',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
)


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'Guest: {self.first_name}, {self.last_name}'


class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    guests = db.relationship(
        'Guest',
        lazy='dynamic',
        secondary=guests,
        backref=db.backref('events', lazy='dynamic'),
    )

    def __repr__(self):
        return f'Event: {self.title}'



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/events')
def events():
    events = Event.query.all()
    return render_template('events.html', events=events)


@app.route('/events/<int:event_id>', methods=['GET', 'POST'])
def register_to_event(event_id):
    event = Event.query.get(event_id)
    if request.method == 'POST':
        guest = Guest(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
        )
        db.session.add(guest)
        db.session.commit()

        event.guests.append(guest)
        db.session.add(event)
        db.session.commit()

    return render_template('registration.html', event=event)