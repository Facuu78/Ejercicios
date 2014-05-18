class Nodo(object):
	def __init__(self, dato = None, proximo = None):
		self.dato = dato
		self.proximo = proximo
	
	def __str__(self):
		return str(self.dato)
	
class Lista_enlazada(object):
	def __init__(self):
		self.primer_elemento = None
		self.ultimo_elemento = None
		self.largo = 0
	
	def __str__(self):
		if(self.largo == 0):
			return "[]"
		
		string_salida = "[ "
		nodo = self.primer_elemento
		
		string_salida += str(nodo.dato)
		nodo = nodo.proximo
		while nodo:
			string_salida += ", " + str(nodo.dato)
			nodo = nodo.proximo
		string_salida += " ]"
		
		return string_salida
	
	def __len__(self):
		return self.largo
	
	def append(self, dato):
		nodo = Nodo(dato)
		
		if(self.primer_elemento == None):
			self.primer_elemento = nodo
		else:
			self.ultimo_elemento.proximo = nodo 
		
		self.ultimo_elemento = nodo
		
		self.largo += 1
	
	def insert(self, indice, nuevo_item):
		if(not str(indice).isdigit()):
			raise TypeError
		if(indice > self.largo and indice < 0):
			raise IndexError
		if(indice == self.largo):
			append(nuevo_item)
		elif(indice == 0):
			nodo_nuevo = Nodo(nuevo_item)
			nodo_nuevo.proximo = self.primer_elemento
			self.primer_elemento = nodo_nuevo
			self.largo += 1
		else:
			nodo_nuevo = Nodo(nuevo_item) 
			nodo_anterior = self.primer_elemento
			nodo_actual = nodo_anterior.proximo
			contador = 1
			while(contador != indice):
				nodo_anterior = nodo_actual
				nodo_actual = nodo_actual.proximo
				contador += 1
			nodo_anterior.proximo = nodo_nuevo
			nodo_nuevo.proximo = nodo_actual
			
			self.largo += 1
			
	def remove(self, item):
		if(self.largo == 0):
			raise ValueError
		nodo = self.primer_elemento
		if(nodo.dato == item):
			self.primer_elemento = nodo.proximo
		else:
			nodo_siguiente = nodo.proximo
			while( nodo_siguiente.dato != item ):
				nodo = nodo_siguiente
				nodo_siguiente = nodo_siguiente.proximo
				if(nodo_siguiente == None):
					raise ValueError
			
			nodo.proximo = nodo_siguiente.proximo
		
		self.largo -= 1
	
	def pop(self, indice = None ):
		if(indice == None):
			indice = self.largo-1
		if(not str(indice).isdigit()):
			raise TypeError
		if(indice >= self.largo and indice < 0):
			raise IndexError
		if(indice == 0):
			valor = self.primer_elemento.dato
			self.primer_elemento = self.primer_elemento.proximo
			return valor
        
		nodo_anterior = self.primer_elemento
		nodo_actual = nodo_anterior.proximo
		contador = 1
		while(contador != indice):
			nodo_anterior = nodo_actual
			nodo_actual = nodo_actual.proximo
			contador += 1
		valor = nodo_actual.dato
		nodo_anterior.proximo = nodo_actual.proximo
		
		self.largo -= 1
		return valor

	def index(self, item):
		nodo = self.primer_elemento
		indice = 0
		if(nodo.dato == item):
			return indice
		while( not (nodo.proximo == None) ):
			nodo = nodo.proximo
			indice += 1
			if(nodo.dato == item):
				return indice

		raise ValueError
	
def main():
	
	lista = Lista_enlazada()
	lista.append(1)
	lista.append(2)
	lista.append(3)
	lista.append(4)
	lista.append(5)
	lista.append(6)

	print lista
	print len(lista)
	print lista.pop(2)
	print lista
	print len(lista)
	print	
	
	raw_input()
main()
