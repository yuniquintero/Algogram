from usuario import Usuario, ListaDoble
from registro_usuarios import Registro_Usuarios

class NodoPila():
	#representacion de cada elemento de la pila
	def __init__(self, elemento, siguiente = None):
		#assert de que cada mensaje sea de la forma "n1: " o "n2: "
		self.elemento = elemento
		self.siguiente = siguiente

	def __str__(self): 
		#esto es para mostrar la conv pero ta fea
		string = "["
		aux = self
		while not aux == None:
			string += "{0},".format(aux.elemento)
			aux = aux.siguiente
		string = string[:-1] + "]" 
		return string

	def __repr__(self):
		return self.__str__()

class Pila():
	# contiene los mensajes que se han enviado entre dos
	# usuarios
	def __init__(self):
		#inicializacion de la pila
		self.nil = NodoPila(None, None)
		self.nil.siguiente = self.nil
		self.count = 0

	def is_empty(self):
		# metodo que verifica si la pila esta vacia
		return self.count == 0

	def push(self, k):
		suc = self.nil.siguiente
		nuevo_mensaje = NodoPila(k, suc)
		self.nil.siguiente = nuevo_mensaje
		self.count += 1

	def pop(self):
		assert (not self.is_empty()), "La cola de mensajes esta vacia."
		m = self.nil.siguiente.elemento
		self.nil.siguiente = self.nil.siguiente.siguiente
		self.count -= 1
		return m


class Chat():
	# tipo de datos que almacena los mensajes que se han enviado
	# entre dos usuarios
	def __init__(self, user1, user2): #cuando registrar usuario este ready verificar
										# que n1 y n2 pertenezcan a esa tabla
										#esto siendo importando la funcion hash y que
										# no devuelva null en la tabla pasandole n1 y n2 
		assert(type(user1) == Usuario and type(user2) == Usuario), "Los datos del constructor de Chat no son de tipo Usuario"
		if user1.nombre.lower() < user2.nombre.lower():
			self.ide = user1.nombre + '-' + user2.nombre
		else:
			self.ide = user2.nombre + '-' + user1.nombre
		self.mensajes = Pila()

	def agregarMensaje(self, u, m):
		# metodo que agrega un elemento a la pila
		assert type(u) == Usuario
		self.mensajes.push(u.nombre + ": " + m)
		
	def mostrarChat(self): #para mostrar el chat
		aux = Pila()
		user1, user2 = self.ide.split('-')
		sep    = "   +{:-^52}+\n".format('-')
		string = "   | {:^50} |\n".format("Chat entre " + user1 + " y " + user2)
		string = sep + string + sep
		while not self.mensajes.is_empty():
			aux.push(self.mensajes.pop())
		while not aux.is_empty():
			mensaje = aux.pop()
			self.mensajes.push(mensaje)
			if mensaje.split(':')[0] == user1:
				string += "   | {:>50} |\n".format(mensaje)
			else:
				string += "   | {:<50} |\n".format(mensaje)
		string += sep
		return string
