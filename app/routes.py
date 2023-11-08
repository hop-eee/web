# -*- coding: utf-8 -*-
from flask import *
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}, language={}'.format(
            form.username.data, form.remember_me.data, form.language.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
