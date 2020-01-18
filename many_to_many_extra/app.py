from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relations2.db'
db = SQLAlchemy(app)

admin = Admin(app)


class Order_Product(db.Model):
    __tablename__ = 'order_product'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer)


class Product(db.Model):
    """ SQLAlchemy Product Model """
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    stock = db.relationship('Order_Product', backref='product', primaryjoin=id == Order_Product.product_id)

class Category(db.Model):
    """ SQLAlchemy Category Model """
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    stock = db.relationship('Order_Product', backref='category', primaryjoin=id == Order_Product.category_id)


admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Order_Product, db.session))

'''
db.create_all()

prod = Product(name="Oreo")
prod1 = Product(name="Hide and Seek")

cate1 = Category(name="biscuit")
cate2 = Category(name="creamy")
cate3 = Category(name="chocolate")

op1 = Order_Product(id=1, category_id=cate1.id, product_id=prod.id, quantity=20)
prod.stock.append(op1)
cate1.stock.append(op1)

op2 = Order_Product(id=2, category_id=cate3.id, product_id=prod.id, quantity=10)
prod.stock.append(op2)
cate3.stock.append(op2)

op3 = Order_Product(id=3, category_id=cate1.id, product_id=prod1.id, quantity=40)
prod1.stock.append(op3)
cate1.stock.append(op3)

db.session.add_all([prod, prod1, cate1, cate2, cate3])
db.session.commit()
'''
# Get all categories a product belongs to
for p in db.session.query(Product).all():
    print (p.name)
    for a in p.stock:
        print (db.session.query(Category).filter_by(id=a.category_id).all())

# Get all products that belong to a cateogory
for c in db.session.query(Category).all():
    print (c.name)
    for a in c.stock:
        print (db.session.query(Product).filter_by(id=a.product_id).all())


if __name__ == "__main__":
    app.run(debug=True)