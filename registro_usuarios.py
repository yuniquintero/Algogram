from usuario import Usuario, ListaDoble, NodoLista
from math import sqrt, floor
import sys
from arrayT import ArrayT

class Registro_Usuarios():
	"""
		Descripcion:
			Clase generadora de objetos cuya utilidad sera guardar
			registros de usuarios para el chat ALGOGRAM
	"""
	def __init__(self, n):
		"""
			Descripcion:
				Funcion constructora de "Registro_Usuarios"

			Parametros:
				n: Tamaño del hash

		"""
		assert type(n) == int and n > 0, "La tabla no puede ser inicializada con 0 slots"
		self.tamano = n
		self.tablaRU = ArrayT(n)
		for i in range(n):
			self.tablaRU[i] = ListaDoble()

	def buscar(self, key, op = 1):
		"""
			Descripcion: 
				Funcion auxiliar, no esta incluida para el proyecto
				Es para verificar y no reusar codigo.

			Parametros:
				key: clave (nombre de usuario) a buscar en la tabla
				op: opcional, para mi uso

			Retorno:
				True si el elemento se encuentra, sino False

		"""	
		h = hash(key) % self.tamano
		aux = self.tablaRU[h].nil.siguiente
		while aux != self.tablaRU[h].nil:
			if aux.elemento.nombre == key:
				if op == 1:
					return True
				else:
					return aux.elemento
			aux = aux.siguiente
		return False

	def agregarUsuario(self, user):
		"""
			Descripcion:
				Funcion que agrega un usuario a la tabla. Si se encuentra no hace nada

			Parametros:
				user: Objeto de tipo usuario a agregar a la tabla

			Retorno:
				True si el usuario no se encontro y se agrego con exito
				False si el usuario se encotraba
		"""
		assert type(user) == Usuario
		if not self.buscar(user.nombre):
			h = hash(user.nombre) % self.tamano
			pred = self.tablaRU[h].nil
			suc = pred.siguiente
			nuevo = NodoLista(user, pred, suc)
			pred.siguiente = nuevo
			suc.anterior = nuevo
			#print(pred, suc)
			return True
		return False

	def eliminarUsuario(self, nombre):
		"""
			Descripcion:
				Funcion que elimina un usuario de la tabla de hash

			Parametros:
				nombre: nombre del usuario a eliminar

			Retorno:
				True si se encontraba y se elimino
				False si no se encontraba, en tal caso no hace nada la funcion
		"""
		assert(type(nombre) == str and len(nombre) > 0)
		if self.buscar(nombre):
			h = hash(nombre) % self.tamano
			aux = self.tablaRU[h].nil.siguiente
			while aux.elemento.nombre != nombre:
				aux = aux.siguiente
			pred = aux.anterior
			suc = aux.siguiente
			pred.siguiente = suc
			suc.anterior = pred
			return True
		return False

	def cargarUsuarios(self, archivo):
		"""
			Descripcion:
				Funcion que recive el path de un archivo y carga
				su contenido a la tabla de hash

			Parametros:
				archivo: path del archivo a cargar

			Retorno:
				un mensaje para indicarle al usuario sobre algo sucedido
		"""
		try:
			assert (type(archivo) == str and len(archivo) > 0)
			with open(archivo, 'r') as f:
				for line in f:
					aux = line.split("\t")
					self.agregarUsuario(Usuario(aux[0], aux[1], aux[2][:len(aux[2]) - 1], ListaDoble()))
			ret = "   Archivo cargado exitosamente"
		except FileNotFoundError:
			ret = "   El archivo especificado no existe"
		except AssertionError:
			ret = "   El archivo especificado en cargarUsuarios es un string vacio"
		return ret
			

	def mostrarRegistro(self):
		"""
			Descripcion:
				Funcion para mostrar el registro de usuarios. 

			Parametros:
				void

			Retorno:
				Un string con el contenido de los usuarios registrados
				en formato tabla de datos.
		"""
		sep    = "   +{:-^33}+\n".format('\0')
		string = sep + "   | {:^30} |\n".format("Registro de Usuarios") + sep
		for i in range(self.tamano):
			aux = self.tablaRU[i].nil.siguiente
			while aux != self.tablaRU[i].nil:
				string += "   | {:30} |\n".format(aux.elemento.__str__())
				aux = aux.siguiente
		string += sep
		return string