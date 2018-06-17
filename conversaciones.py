from chat import Chat
from usuario import ListaDoble, Usuario, NodoLista
from arrayT import ArrayT

class Conversaciones():
	"""
		Descripcion:
			Clase creadora de tablas de hash. Soporta las funciones que estan abajo.
			Esta tabla contendra un registro de los chats del servicio ALGOGRAM
	"""
	def __init__(self, n):
		"""
			Descripcion:
				Funcion que crea la tabla de hash de tamano 'n'

			Parametros:
				n: Tamaño del hash a crear
		"""
		assert type(n) == int and n > 0, "La tabla no puede ser inicializada con 0 slots"
		self.tamano = n
		self.tablaC = ArrayT(n)
		for i in range(n):
			self.tablaC[i] = ListaDoble()

	def buscarConversacion(self, ide):
		"""
			Descripcion:
				Funcion que busca una clave en la tabla y retorna su dato correspondiente.
				Retorna None si no lo encuentra.

			Parametros:
				ide: clave a buscar en la tabla de hash

			Retorno:
				None en caso de que no se encuentre, sino un APUNTADOR a la conversacion
		"""
		assert(type(ide) == str and len(ide) > 0)
		h = hash(ide) % self.tamano
		aux = self.tablaC[h].nil.siguiente
		while aux != self.tablaC[h].nil:
			if aux.elemento[0] == ide:
				return aux.elemento[1]
			aux = aux.siguiente
		return None
		

	def agregarConversacion(self, c):
		"""
			Descripcion:
				Funcion que primero chequea si una conversacion no existe.
				En caso afirmativo la agrega, si no reemplaza el chat existente
			Parametros:
				c: Objeto de tipo 'Chat' que se agregara a la tabla

			Retorno:
				True en caso de que se agrego con exito, False en caso de que se reemplazo alguno
		"""
		assert type(c) == Chat
		h = hash(c.ide) % self.tamano
		bus = self.buscarConversacion(c.ide)
		if bus != None:
			bus.mensajes = c.mensajes
			return False
		else:
			nuevo_chat = NodoLista((c.ide, c), self.tablaC[h].nil, self.tablaC[h].nil.siguiente)
			suc = self.tablaC[h].nil.siguiente
			pred = self.tablaC[h].nil
			suc.anterior = nuevo_chat
			pred.siguiente = nuevo_chat
			return True
