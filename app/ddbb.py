#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient("mongodb+srv://manolorooter:Iv6u7PQjQjcsjBY7@macramehuetorvega.vuchl.mongodb.net/PortalRestaurantes?retryWrites=true&w=majority")

#Accedemos a la BBDD
db = client.PortalRestaurantes

def getMenu(keys):
	res = [] #Creamos un array para cada key
	for i in keys:
		dict_i = {i:[]} #Creamos un diccionario con clave key y valor un array
		for j in db.ResturanteLineal.find({'dishtype':i}): #Guardamos en el array cada plato o bebida
			dict_i[i].append(j)
		res.append(dict_i)
	return res