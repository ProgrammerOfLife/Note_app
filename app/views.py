from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():

	user = {'Name' : input("Please what is your name")}
	
	return render_template('index.html',  user=user)

@app.route('/note', methods=['GET', 'POST'])
def Create_Note():
	form = LoginForm()
	return render_template('Note.html', title= 'Sign In', form = form)