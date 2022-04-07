from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    vallas= db.relationship('Valla', backref='user', lazy=True)   # relationship
    orders= db.relationship('Order', backref='user', lazy=True)    # relationship
    clients= db.relationship('Client', backref='user', lazy=True)    # relationship

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
        
class Order(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    order_price = db.Column(db.Integer, unique=False)
    register_date = db.Column(db.Date, unique=False, nullable=False)
    start_date = db.Column(db.Date, unique=False, nullable=False)
    finish_date = db.Column(db.Date, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  #FK
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)  #FK
    vallas= db.relationship('Valla', backref='order', lazy=True)   # relationship
    payment= db.relationship('Payment', backref='order', lazy=True)    # relationship
    
    def __repr__(self):
        return '<Order %r>' % self.id
    
    def serialize(self):
        return {
            "order_id": self.id,
        }
class Payment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    due_date = db.Column(db.Date, unique=False, nullable=True)
    payment_date = db.Column(db.Date, unique=False, nullable=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)  #FK
    
    def __repr__(self):
        return '<Payment %r>' % self.id
    
    def serialize(self):
        return {
            "payment_id": self.id,
        }        
        
class Valla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(150), unique=False, nullable=False)
    size = db.Column(db.String(50), unique=False, nullable=False)
    structure = db.Column(db.String(50), unique=False, nullable=False)
    price_low = db.Column(db.Float, unique=False, nullable=True)
    price_high = db.Column(db.Float, unique=False, nullable=True)
    view = db.Column(db.String(150), unique=False, nullable=False)
    route = db.Column(db.String(150), unique=False, nullable=False)
    status = db.Column(db.String(40), unique=False, nullable=True)
    register_date = db.Column(db.Date, unique=False, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False) #FK
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False) #FK
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #FK
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False) #FK
    
    def __repr__(self):
        return '<Valla %r>' % self.valla_code

    def serialize(self):
        return {
            "id": self.id,
            "valla_code": self.code,
            "valla_name": self.name,
            "size": self.size,
            "structure": self.structure,
            "price_low": self.price_low,
            "price_high": self.price_high,
            "view": self.view,
            "route":self.route,
            "status": self.status,
            "register_date": self.register_date, 
        }

class Owner(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name= db.Column(db.String(150), unique=False, nullable=False)
    phone= db.Column(db.String(30), unique=True, nullable=False)
    email= db.Column(db.String(30), unique=True, nullable=False)
    company= db.Column(db.String(80), unique=True, nullable=True)
    vallas= db.relationship('Valla', backref='owner', lazy=True)   # relationship
    
    def __repr__(self):
        return '<Owner %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "owner_code": self.code,
            "owner_name": self.name,
            "phone": self.phone,
            "email": self.email, 
            "company": self.company,
        }
        
class Client(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name= db.Column(db.String(150), unique=False, nullable=False)
    phone= db.Column(db.String(30), unique=True, nullable=False)
    email= db.Column(db.String(30), unique=True, nullable=False)
    company= db.Column(db.String(80), unique=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #FK
    vallas= db.relationship('Valla', backref='client', lazy=True)   # relationship
    orders= db.relationship('Order', backref='client', lazy=True)    # relationship
    
    
    def __repr__(self):
        return '<Client %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "owner_code": self.code,
            "owner_name": self.name,
            "phone": self.phone,
            "email": self.email, 
            "company": self.company,
        }        

