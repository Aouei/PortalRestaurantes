#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import render_template, url_for, redirect, flash, request
from .utils import getPlatos
from .ddbb import initializeBBDD, getMenu
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

initializeBBDD()

dishTypes = ['Entrantes', 'Segundos', 'Postres', 'Bebidas']

@app.route('/')
def home():
	return render_template('portal.html', R1 = url_for('R1'), R2 = url_for('R2'), R3 = url_for('R3'))

@app.route('/restaurante1')
def R1():
	return render_template('restaurante1.html', menu = getMenu(dishTypes), menuS = dishTypes[0], date=datetime.today().strftime('%Y-%m-%d'))

@app.route('/restaurante2')
def R2():
	return render_template('platos.html')

@app.route('/restaurante3')
def R3():
	return render_template('platos.html')

@app.route('/platos')
def platos():
	return render_template('platos.html', primero = getPlatos('IMG/Platos/primero', 3), 
										  segundo = getPlatos('IMG/Platos/segundo', 3), 
										  postre = getPlatos('IMG/Platos/postre', 3), contexto = 'postre')

@app.route('/menus')
def menus():
	return render_template('menus.html')

@app.route('/contacto')
def contacto():
	return render_template('contacto.html')

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('home'))