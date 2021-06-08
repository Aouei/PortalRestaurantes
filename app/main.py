#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import render_template, url_for, redirect, flash, request
from .ddbb import getMenu
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
	return render_template('portal.html', R1 = url_for('R1'), R2 = url_for('R2'), R3 = url_for('R3'))

@app.route('/restaurante1')
def R1():
	dishTypes = ['Entrantes', 'Segundos', 'Postres', 'Bebidas']
	return render_template('restaurante1.html', menu = getMenu(dishTypes), menuS = dishTypes[0], date=datetime.today().strftime('%Y-%m-%d'))

@app.route('/restaurante2')
def R2():
	return render_template('platos.html')

@app.route('/restaurante3')
def R3():
	return render_template('platos.html')

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('home'))