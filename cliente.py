from usuario import Usuario, ListaDoble
from registro_usuarios import Registro_Usuarios
from chat import Chat
from conversaciones import Conversaciones
import subprocess as sp
import sys, time
from arrayT import ArrayT

"""
	Proyecto3

	Descripcion: Elaboracion de un chat mediante estructuras de datos elementales

	SUGERENCIA: Coloque el terminal en pantalla grande para una mejor experiencia.

	Autores:
		Yuni Quintero 14-10880
		German Robayo 14-10924

	Profesor:
		Guillermo Palma
"""



# Variables de interfaz
titulo =  "\v    █████╗ ██╗      ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗\n"
titulo +=   "   ██╔══██╗██║     ██╔════╝ ██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║\n"
titulo +=   "   ███████║██║     ██║  ███╗██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║\n"
titulo +=   "   ██╔══██║██║     ██║   ██║██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║\n"
titulo +=   "   ██║  ██║███████╗╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║\n"
titulo +=   "   ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝\n"
msj = ""
datos = ArrayT(6)
datos[0] = " 1. Registrarse"
datos[1] = " 2. Iniciar sesion"
datos[2] = " 3. Cargar Usuarios"
datos[3] = " 4. Eliminar usuario"
datos[4] = " 5. Cargar caritas"
datos[5] = " 6. Salir"
sep = "   +{:-^34}+".format('\0')
menu_ingreso = sep
menu_ingreso += "\n   |{:32} |\n   |{:32} |\n   |{:32} |\n   |{:32} |\n   \
|{:32} |\n   |{:32} |\n".format(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])
menu_ingreso += sep + '\n'
datos = ArrayT(8)
datos[0] = "1. Agregar contacto"
datos[1] = "2. Eliminar contacto"
datos[2] = "3. Mostrar Contactos"
datos[3] = "4. Ver conversacion" 
datos[4] = "5. Enviar mensaje"
datos[5] = "6. Mostrar caritas"
datos[6] = "7. Mostrar usuarios registrados"
datos[7] = "8. Cerrar sesion"
cargado = False
menu_usuario = sep + "\n   | {:32}|\n   | {:32}|\n   | {:32}|\n   | {:32}|\n   | {:32}|\n\
   | {:32}|\n   | {:32}|\n   | {:32}|\n".format(datos[0], datos[1], \
datos[2], datos[3], datos[4], datos[5], datos[6], datos[7]) + sep + '\n'

# Variables de funcionamiento
ret = None
tablaRU = Registro_Usuarios(20)
tablaC = Conversaciones(20)
menu_principal = True
menu_inicio = False
usuario_actual = None


def cargarCaritas(archivo):
	"""
		Descripcion:
			Funcion que carga un archivo con las caritas que se usaran 
			en el chat ALGOGRAM

		Parametros:
			archivo: path del archivo
	"""
	try:
		global ret, msj, cargado
		with open(archivo, 'r') as f:
			for line in f:
				aux = line.split("\t")
				n = len(aux)
			ret = ArrayT(n)
			print(aux)
			for i in range(n):
				stop = 0
				for j in range(len(aux[i])-1, -1, -1):
					if aux[i][j] == '=':
						stop = j
						break
				ret[i] = aux[i][0:stop]
		msj = "   Caritas agregadas"
		cargado = True
	except FileNotFoundError:
		msj = "   El archivo especificado no se ha encontrado"

def mostrarCaritas():
	"""
		Descripcion:
			Funcion que retorna un string con las caritas

		Parametros:
			void
	"""
	string = "   "
	for i in range(len(ret)):
		string += ret[i] + ', '
	string = string[:len(string) - 2]
	return string

def getIde(nombre1, nombre2):
	"""
		Descripcion:
			Funcion para computar el ide del chat entre dos usuarios

		Parametros:
			nombre1: Nombre del primer usuario
			nombre2: Nombre del segundo usuario
	"""
	if nombre1.lower() < nombre2.lower():
		return nombre1 + "-" + nombre2
	else:
		return nombre2 + "-" + nombre1

def menuPrincipal():
	global menu_principal, menu_inicio, usuario_actual, timing, banner, msj
	print(titulo)
	print(menu_ingreso)
	print(msj)
	msj = ""
	try:
		op = int(input("\n   Ingrese su opcion: "))
		assert 1 <= op <= 6

		# Parte de registro de usuario.
		if op == 1:
			nombre = input("\n   Ingrese su nombre: ")
			assert len(nombre) > 0
			if tablaRU.buscar(nombre):
				msj = "   El usuario ya se encuentra registrado."
				
			else:
				password = input("   Ingrese su contrasena: ")
				assert len(password)
				cpass = input("   Verifique su contrasena: ")
				if password == cpass: 
					telefono = input("   Ingrese su numero de telefono: ")
					nuevo = Usuario(nombre, password, telefono, ListaDoble())
					tablaRU.agregarUsuario(nuevo)
					msj = "   Usuario agregado con exito"
				else:
					msj = "   Contrasena incorrecta"	
		
		# Parte del inicio de sesion, se verifica que el usuario este registrado y que
		# coincidan los passwords
		elif op == 2:
			nombre = input("   Ingrese su nombre: ")
			if tablaRU.buscar(nombre):
				usuario_actual = tablaRU.buscar(nombre, 2)
				password = input("   Ingrese su contrasena: ")
				assert usuario_actual.password == password
				menu_principal = False
				menu_inicio = True
			else:
				
				msj = "   El usuario ingresado no esta registrado"
		
		# Parte para cargar archivo con usuarios para la aplicacion
		elif op == 3:
			archivo = input("   Ingrese la direccion de su archivo: ")
			msj = tablaRU.cargarUsuarios(archivo)
			
		# Parte para eliminar usuarios
		elif op == 4:
			nombre = input("   Ingrese el nombre del usuario a eliminar: ")
			assert len(nombre) > 0
			if tablaRU.eliminarUsuario(nombre):
				msj = "   Usuario eliminado"
			else:
				msj = "   El usuario no se encuentra"
			
		# Parte para cargar el archivo de caritas de la aplicacion
		elif op == 5:
			archivo = input("   Ingrese el nombre del archivo: ")
			cargarCaritas( archivo )
		
		# Parte para confirmacion de salida	
		elif op == 6:
			conf = input("    Esta seguro que desea salir? (s/n): ")
			while conf != 's' and conf != 'n':
				print("   Solo puede ingresar 's(Si)' o 'n(No)'")
				conf = input("   Esta seguro que desea salir? (s/n):   ")
			if conf == 's':
				sp.call("clear", shell = True)
				sys.exit()
	except AssertionError:
		if op == 1:
			msj = "   Alguno de sus datos esta ingresado de manera incorrecta\n"
			msj += "   Telefono solo debe contener numeros entre 0 y 9\n"
			msj += "   Nombre y Password deben ser distintos de vacio"
		elif op == 2:
			msj = "   No coincide la contraseña del usuario '{:}'".format(nombre)
		elif op == 3:
			pass
		elif op == 4:
			msj = "   El nombre no puede ser vacio"
		else:
			msj = "   Solo puede ingresar un numero del 1 al 5"
		
	except ValueError:
		msj = "   No ingreso un numero"

def menuInicio():
	global menu_principal, menu_inicio, usuario_actual, msj, banner
	print("   +{0:-^37}+\n   | Bienvenido(a): {1:^19s} |\n   +{0:-^37}+\n".\
	format('\0', usuario_actual.nombre))
	print(menu_usuario)
	print(msj)
	msj = ""
	try:
		op = int(input("\n   Ingrese su opcion: "))
		assert 1 <= op <= 8
		
		# Parte del registro del usuario en la lista de contactos del usuario
		if op == 1:
			nombre = input("   Ingrese el nombre del usuario: ")
			assert len(nombre) > 0
			contacto_nuevo = tablaRU.buscar(nombre, 2)
			if type(contacto_nuevo) == Usuario:
				if usuario_actual.agregarContacto(contacto_nuevo):
					msj = "   El usuario fue agregado a tu lista de contactos"
				else:
					msj = "   El usuario ya se encuentra en su lista de contactos"
			else:
				msj = "   El usuario que desea agregar no esta registrado"
		
		# Parte de eliminacion de usuario de la lista de contactos	
		elif op == 2:
			nombre = input("Ingrese el nombre del usuario: ")
			assert len(nombre)
			if usuario_actual.eliminarContacto(nombre):
				msj = "   Usuario eliminado"
			else:
				msj = "   El usuario no se encuentra en la lista de contactos"
		
		# Parte para mostrar los contactos del usuario
		elif op == 3:
			msj = usuario_actual.mostrarContactos()
			
		# Parte para mostrar el chat entre dos usuarios
		# Los imprime en orden de llegada
		elif op == 4:
			nombre = input("   Ingrese el nombre del usuario con quien desea saber su chat: ")
			assert len(nombre) > 0
			if tablaRU.buscar(nombre):
				if usuario_actual.buscarContacto(nombre):
					ide = getIde(usuario_actual.nombre, nombre)
					chat = tablaC.buscarConversacion(ide)
					if chat != None:
						msj = chat.mostrarChat()
					else:
						msj = "   No existe chat entre estos dos usuarios"
				else:
					msj = "   El usuario no se encuentra en la lista de contactos"
			else:
				msj = "   El usuario no se encuentra registrado"
			
		# Parte para enviar un mensaje al chat de un usuario especifico
		elif op == 5:
			nombre = input("   Ingrese el nombre del destinatario: ")
			if tablaRU.buscar(nombre):
				usuario_dest = usuario_actual.buscarContacto(nombre, 2)
				if usuario_dest != None:
					mensaje = input("   Ingrese el mensaje a enviar: ")
					ide = getIde(usuario_actual.nombre, usuario_dest.nombre)
					chat = tablaC.buscarConversacion(ide)
					if chat != None:
						chat.agregarMensaje(usuario_actual, mensaje)
					else:
						chat = Chat(usuario_actual, usuario_dest)
						chat.agregarMensaje(usuario_actual, mensaje)
						tablaC.agregarConversacion(chat)
					msj = "   Mensaje enviado con exito"
				else:
					msj = "   El usuario no se encuentra en tu lista de contactos"
			else:
				msj = "   El usuario no se encuentra registrado"
		
		# Para mostrar las caritas
		elif op == 6:
			if cargado:
				msj = mostrarCaritas()
			else:
				msj = "   No hay un paquete de caritas disponible.\nPara agregarlo regrese al menu principal"
		
		# Para mostrar todos los usuarios actuales
		elif op == 7:
			msj = tablaRU.mostrarRegistro()
		
		# Confirmacion de cierre de sesion
		elif op == 8:
			conf = input("   Esta seguro que desea salir? (s/n): ")
			while conf != 's' and conf != 'n':
				print("   Solo puede ingresar 's(Si)' o 'n(No)'")
				conf = input("   Esta seguro que desea salir? (s/n): ")
			if conf == 's':
				menu_principal = True
				menu_inicio = False
	except ValueError:
		msj = "   No ingreso un numero entero"
	except AssertionError:
		if op == 1 or op == 2 or op == 4:
			msj = "   El nombre del usuario no puede ser vacio"
		else:
			msj = "   Datos ingresados de manera incorrecta. Debe ser un numero"
		



def main():
	global banner
	while True:
		sp.call("clear", shell = True)
		if menu_principal:
			menuPrincipal()
		elif menu_inicio:
			menuInicio()

if __name__ == '__main__':
	main()