# coding:"utf-8"

# \w -> cualquier unicode letra por letra
# \W -> lo que no sea unicode
# \s -> whitespace, space, tabs, etc
# \S -> lo que no sea whitespace, tabs, space, etc
# \d -> número 0 al 9
# \D -> lo que no sea número
# \b -> extremo de la palabra
# \B -> no en el extremo de la palabra

# {3} -> cuenta exactamente 3 ocurrencias del patron
# {,3} -> cuenta de 0 a 3 ocurrencias del patron, igual que slicing
# ? -> opcional, de 0 a 1 vez
# * -> al menos 0 veces
# + -> al menos una vez

# [] -> define un set
# [a-z] -> set con rango, vale para minusculas, mayusculas y números
# [^a-d] -> el techito implica no encontrar esos carateres

# Flags, pasadas como parametro extra
# | -> permite pasar más flags flags
# re.IGNORECASE, re.I -> ignora mayusculas y minusculas
# re.VERBOSE , re.X-> multiple lines

import re

with open("names.txt", encoding="utf-8") as names_file:
	data = names_file.read()


last_name = r'Love'
first_name = r'Kenneth'

#Python offers two different primitive operations based on regular expressions: re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in the string 

# Match encuentra la primera ocurrencia del caso
print(re.match(last_name, data))

# Search busca en cualquier posición del string
print(re.search(first_name, data))

# buscamos un patron específico de números, retornamos la primera ocurrencia
print(re.search(r'\d\d\d-\d\d\d\d', data))

# repetimos pero con tamaños variables y parentesis opcionales, findall encuentra todos
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

# Buscamos nombres de manera específica
print(re.search(r'\w+, \w+', data))

# Encuentra todos los nombres pero también las profesiones
print(re.findall(r'\w+, \w+', data))

# Encuentra también los nombres sin apellido
print(re.findall(r'\w*, \w+', data))

# Encuentra los emails de manera burda
# [todos los álpha, los números, los simbolos "+", "-" y "."  ]en varias ocurrencias @ [lo mismo pero sin "-"]
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

# Encuentra todas las ocurrencias de la palabra treehouse aunque está este en mayus o minus
print(re.findall(r'\b[trehous]{9}\b', data, re.I))

# Todos los dominios de email pero sin la extension gov si la encuentra
print(re.findall(r"""
	\b@[-\w\d.]*  # Primero un limite de palabra, luego un "@" y por último cualquier cantidad de palabras
	[^gov\t]+  # Ignora una o mas instancias de las letras "g","o" o "v" y los tabs
	\b 
	"""	, data, re.VERBOSE | re.I))

# Nombres y trabajo

print(re.findall(r"""
	\b[-\w]*, # limite, 1+ guion o caracter y una coma
	\s # 1 espacio, usamos este ya que re.X ignora los " " que no están en sets
	[-\w ]+ # 1+ guion y caracter y un espacio explícito
	[^\t\n] # ignora tabs y nuevas lineas
"""
, data, re.X ))







