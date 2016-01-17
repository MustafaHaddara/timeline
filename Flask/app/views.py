from flask import render_template, flash, redirect, Response
from app import app
from .forms import LoginForm
import sys
import os
sys.path.append(os.path.abspath('..'))
import cal

uname=""
pwd=""
downloaded=False

@app.route('/about')
def about():
	#user = {'nickname':'Sheri'} #fake user
	return render_template('about.html', title='About')

@app.route('/downloading')
def downloading():
	global downloaded
	if downloaded:
		downloaded = False
		return get_file()
	else:
		downloaded = True
		return render_template('downloading.html', title='Downloading')

# @app.route('/file')
def get_file():
	global uname, pwd
	file_data = cal.build_cal(uname, pwd)
	old_name = uname
	uname = ""
	pwd = ""
	generator = (line for line in file_data)
	return Response(generator, mimetype="text/calendar", headers={"Content-Disposition":"attachment;filename=%s.ics" % (old_name)})

@app.route('/', methods = ['GET','POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
	global uname, pwd
	form = LoginForm()
	if form.validate_on_submit():
		uname = form.macid.data
		pwd = form.password.data
		return redirect('/downloading')
	else:
		flash("Invalid Login, please try again")
	return render_template('login.html', title='Sign In', form=form)
