#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pickleshare import PickleShareDB
from flask import url_for
import csv

DATABASE = 'BBDD'

db = PickleShareDB(DATABASE)
db.clear()

def initializeBBDD():

	with open('./app/static/R1/dishes.csv', 'r') as file:
		read = csv.reader(file)

		for rows in read:
			data = rows[0].split(";")

			db[data[0]] = db.get(data[0], [])
			db[data[0]].append({'name':data[1], 'ingredients':data[2], 'price':data[3]})

		for i in db:
			db[i] = db[i]

def getMenu(keys):
	return [{i:db[i]} for i in keys]