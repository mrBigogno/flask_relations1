from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relations.db'
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)
admin = Admin(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

admin.add_view(ModelView(Person, db.session))
admin.add_view(ModelView(Pet, db.session))

if __name__ == '__main__':
    app.run(debug=True)
'''

Para inserir uma person no banco:
    gustavo = Person(name='Gustavo')
    db.session.add(gustavo)

Para inserir um pet:
    spot = Pet(name='Spot', owner=gustavo)         (backref='owner')
    db.session.add(spot)

Para imprimir os pets de uma person:
    for pet in gabriela.pets:
        print(pet.name)

Para imprimir o person de um pet:
    brian.owner.name

'''
