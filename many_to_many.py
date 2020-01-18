from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relations2.db'
db = SQLAlchemy(app)

subs = db.Table('subs',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.channel_id'))
)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    subscriptions = db.relationship('Channel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))

class Channel(db.Model):
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(20))

'''

Para inserir um usuário no banco:
    user1 = User(name='Anthony')
    db.session.add(user1)

Para inserir um channel no banco:
    channel1 = Channel(channel_name='Pretty Printed')
    db.session.add(channel1)

Relacionar um usuario com um canal:
    channel1.subscribers.append(user1)      (backref='subscribers')
    channel1.subscribers.append(user3)

Imprimir os inscritos de um canal:
    for user in channel1.subscribers:
        print(user.name)

Imprimir as inscrições de um usuário:
    for channel in user4.subscriptions:
        print(channel.channel_name)

'''
