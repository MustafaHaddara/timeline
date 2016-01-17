from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
import sys
import os
sys.path.append(os.path.abspath('..'))
import cal

@app.route('/about')
def about():
	#user = {'nickname':'Sheri'} #fake user
	return render_template('about.html', title='About')

@app.route('/downloading')
def downloading():
	return render_template('downloading.html', title='Downloading')


@app.route('/', methods = ['GET','POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		print "macid:", form.macid.data
		print "passw:", form.password.data
		return cal.build_cal(form.macid.data, form.password.data)
		#return redirect('/downloading')
	else:
		flash("Invalid Login, please try again")
	return render_template('login.html', title='Sign In', form=form)
