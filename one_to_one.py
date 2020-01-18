from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relations3.db'
db = SQLAlchemy(app)

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    child = db.relationship('Child', backref='parent', uselist=False)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), unique=True)

'''
    parent = Parent(name='parent')
    chlid = Child(name='Child 1', parent=parent)
    db.session.add(parent)
    db.session.add(chlid)
    db.session.commit()

    Sempre que um child é relacionado a um parent, os outros child que eram
    relacionados ao parent deixam de se relacionar e apenas o último se relaciona (unique=True)

    child_two = Child(name='Child 2', parent=parent)
    db.session.add(child_two)
    db.session.commit()

    child_three = Child(name='Child 3', parent=parent)
    db.session.add(child_three)
    db.session.commit()

    chlid.parent (NULL)
    child_two.parent (NULL)
    parent.child (<Child 3>)
    parent.child.name ('Child 3')
'''
