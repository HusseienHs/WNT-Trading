from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class InvoiceForm(FlaskForm):
    client = StringField('Client Name', validators=[DataRequired()])
    items = StringField('Items (comma-separated)', validators=[DataRequired()])
    total = FloatField('Total Amount', validators=[DataRequired()])
    submit = SubmitField('Generate Invoice')

class PurchaseForm(FlaskForm):
    supplier = StringField('Supplier', validators=[DataRequired()])
    items = StringField('Items (comma-separated)', validators=[DataRequired()])
    total = FloatField('Total Amount', validators=[DataRequired()])
    submit = SubmitField('Log Purchase')

class SaleForm(FlaskForm):
    client = StringField('Client Name', validators=[DataRequired()])
    items = StringField('Items (comma-separated)', validators=[DataRequired()])
    total = FloatField('Total Amount', validators=[DataRequired()])
    submit = SubmitField('Log Sale')

class EmployeePaymentForm(FlaskForm):
    employee = StringField('Employee Name', validators=[DataRequired()])
    salary = FloatField('Salary', validators=[DataRequired()])
    submit = SubmitField('Record Payment')
