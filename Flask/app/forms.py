from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
	macid = TextField('MAC ID', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

