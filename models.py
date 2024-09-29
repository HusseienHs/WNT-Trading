from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(100), nullable=False)
    items = db.Column(db.String(200), nullable=False)
    total = db.Column(db.Float, nullable=False)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(100), nullable=False)
    items = db.Column(db.String(200), nullable=False)
    total = db.Column(db.Float, nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(100), nullable=False)
    items = db.Column(db.String(200), nullable=False)
    total = db.Column(db.Float, nullable=False)

class EmployeePayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
