from os import listdir
from flask import url_for

def dividirEnColumnas(datos, columnas):
	resultado, indices = [], list(enumerate(datos))

	for fila in range( len(indices)//columnas + 1 ):
		aux = []

		for columna in range(columnas):
			indice = columna + columnas*fila

			if indice >= len(indices):
				break

			aux.append(datos[indices[indice][1]])

		resultado.append(aux)
		aux = []
	else:
		if len(aux) != 0:
			resultado.append(aux)

	return resultado

def getPlatos(carpeta, columnas):
	platos = {}

	for plato in listdir("./app/static/" + carpeta):
		aux = plato.replace('.png','').replace('.jpg','')
		platos[aux] = platos.get(aux, {0:url_for('static', filename = carpeta + '/' + plato)})

	return(dividirEnColumnas(platos, columnas))