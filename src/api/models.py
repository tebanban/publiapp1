from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
        
class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    owner = db.Column(db.String(150), unique=False, nullable=False)
    size = db.Column(db.String(50), unique=False, nullable=False)
    type = db.Column(db.String(50), unique=False, nullable=False)
    price_low = db.Column(db.Integer, unique=False, nullable=True)
    price_high = db.Column(db.Integer, unique=False, nullable=True)
    view = db.Column(db.String(50), unique=False, nullable=False)
    route = db.Column(db.String(150), unique=False, nullable=False)
    start_date = db.Column(db.Date, unique=False, nullable=True)
    due_date = db.Column(db.Date, unique=False, nullable=True)
    client = db.Column(db.String(150), unique=False, nullable=True)
    status = db.Column(db.String(40), unique=False, nullable=True)
    register_date = db.Column(db.Date, unique=False, nullable=False)
    register_user = db.Column(db.String(60), unique=False, nullable=True)


    def serialize(self):
        return {
            "id": self.id,
            "code": self.code,
            "owner": self.owner,
            "size": self.size,
            "type": self.type,
            "price_low": self.price_low,
            "price_high": self.price_high,
            "view": self.view,
            "route":self.route,
            "start_date": self.start_date,
            "due_date": self.due_date,
            "client": self.client,
            "status": self.status,
            "register_date": self.register_date,
            "register_user": self.register_user,
             
        }