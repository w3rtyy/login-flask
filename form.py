from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class Register(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=4, max=20)])
    Lname = StringField("Last Name", validators=[DataRequired(), Length(min=4, max=20)])
    bday = DateField('DatePicker', format='%d-%m-%Y')
    gender = SelectField('Gender', choices=[('1', 'Male'), ('2', 'Female')])
    email_add = EmailField ("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Passowrd", validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField("Confirm Passowrd", validators=[DataRequired(), Length(min=5, max=20), EqualTo("password")])
    submit = SubmitField("Sign up")

class Login(FlaskForm):
    email_add = EmailField ("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Passowrd", validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField("Login")