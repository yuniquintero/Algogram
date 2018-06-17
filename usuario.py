class NodoLista():
	"""
		Descripcion:
			Clase creadora de objetos de tipo Nodo
			para la lista circular doblemente enlazada
	"""
	def __init__(self, e, a, s):
		"""
			Descripcion:
				FUncion constructora de nodos

			Parametros:
				e: elemento, dato que contendra el nodo
				a: APUNTADOR al anterior
				s: APUNTADOR al siguiente
		"""
		self.elemento = e
		self.anterior = a
		self.siguiente = s

class ListaDoble():
	"""
		Descripcion:
			Clase creadora de objetos de tipo ListaDoble
			Estos son listas circulares doblemente enlazadas
	"""
	def __init__(self):
		"""
			Descripcion:
				Funcion constructora

			Parametros:
				void
		"""
		self.nil = NodoLista(None, None, None)
		self.nil.siguiente = self.nil
		self.nil.anterior = self.nil

	def empty(self):
		return self.nil.siguiente == self.nil

class Usuario():
	"""
		Descripcion:
			Clase creadora de objetos de tipo Usuario
			para facilitar el uso de la aplicacion ALGOGRAM
	"""
	def __init__(self, nombre, password, telefono, contactos):
		"""
			Descripcion:
				Constructora de Usuario

			Parametros:
				nombre: String con el nombre del usuario
				password: String con el password del usuario
				telefono: String con el telefono del usuario
				contactos: ListaDoble con los contactos del usuario
		"""
		assert type(nombre) == str and type(password) == str and type(telefono) == str and type(contactos) == ListaDoble
		assert(len(nombre) > 0 and len(password) > 0 and len(telefono) > 0 \
			and all ('0' <= letra <= '9' for letra in telefono))

		self.nombre = nombre
		self.password = password
		self.telefono = telefono
		self.contactos = contactos 

	def __str__(self):
		"""
			Descripcion:
				Funcion que retorna un string que representa al 
				usuario

			Parametros:
				void
		"""
		string =  self.nombre + ", " + self.telefono 
		return string

	def buscarContacto(self, nombre, p=1):
		"""
			Descripcion:
				Funcion que busca un nombre de un contacto en la lista de contactos 
				del usuario.

			Parametros:
				nombre: Nombre del contacto a buscar
				p: opcional, si es 1 es el defecto, sino retorna otra cosa 

			Retorno:
				Si p=1 retorna True si se encuentra, si no False
				Si p!=1 retorna un puntero al usuario encontrado, si no None
		"""
		aux = self.contactos.nil.siguiente
		while aux != self.contactos.nil:
			if aux.elemento.nombre == nombre:
				if p == 1:
					return True
				else:
					return aux.elemento
			aux = aux.siguiente
		if p == 1:
			return False
		else:
			return None

	def es_menor_nombre(self, other):
		"""
			Descripcion:
				Funcion auxiliar para computar la comparacion de dos usuarios

			Parametros:
				other: Otro usuario a comparar
		"""
		return self.nombre.lower() < other.nombre.lower()
	
	def empty(self):
		"""
			Descripcion:
				Funcion auxiliar para ver si la lista de contactos esta vacia o no

			Parametros:
				void

		"""
		return self.contactos.nil.siguiente == self.contactos.nil

	def agregarContacto(self, user):
		"""
			Descripcion:
				Funcion que agrega un contacto a la lista de usuario de un usuario

			Parametros:
				user: Usuario a agregar

			Retorno:
				True si el elemento se agrego
				False si no se agrego
				No pueden haber repetidos 
		"""
		assert type(user) == Usuario, "No se esta agregando algo de tipo usuario a la lista de contactos de {:s}".format(self.nombre)
		##
		## Codigo de verificacion de user.
		##
		nuevo = NodoLista(user, self.contactos.nil, self.contactos.nil)
		suc = self.contactos.nil.siguiente
		while suc != self.contactos.nil and suc.elemento.es_menor_nombre(user):
			suc = suc.siguiente
		if suc != self.contactos.nil and suc.elemento.nombre == user.nombre: 
			return False
		pred = suc.anterior
		pred.siguiente = nuevo
		suc.anterior = nuevo
		nuevo.anterior = pred
		nuevo.siguiente = suc
		return True


	def eliminarContacto(self, nombre):
		"""
			Descripcion:
				Funcion que recibe un nombre y procede a intentar
				eliminar el usuario con ese nombre de la lista de
				contactos

			Parametros:
				nombre: Nombre del usuario a eliminar

			Retorno:
				Si se encuentra, se elimina y retorna True
				Si no, False y no modifica la lista
		"""
		assert (type(nombre) == str), "Debe ingresar un string a eliminarContacto."
		assert( len(nombre) > 0 ), "El nombre en eliminarContacto no puede ser vacio"
		a = self.contactos.nil.siguiente
		while a != self.contactos.nil:
			if a.elemento.nombre == nombre:
				pred = a.anterior
				suc = a.siguiente
				pred.siguiente = suc
				suc.anterior = pred
				return True
		return False


	def mostrarContactos(self):
		"""
			Descripcion:
				Funcion que muestra los contactos del el usuario

			Parametros:
				void

			REtorno:
				Un string con los usuarios en la lsita de contactos
				en formato tabla
		"""
		a = self.contactos.nil.siguiente
		#string = "| Usuarios de: {:>s} |".format(self.nombre)
		#sep = '-' for i in range(len(string) - 2)
		sep    = "   +--------------------------------------+\n"
		string = sep + "   | Lista de contactos de: " + self.nombre.center(14) + '|\n' + sep
		while a != self.contactos.nil:
			string += "   | " + a.elemento.__str__().center(36) + ' |\n'
			a = a.siguiente
		string += sep
		return string
