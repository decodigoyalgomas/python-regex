import re

with open("names.txt", encoding="utf-8") as names_file:
	data = names_file.read()

# Match encuentra solo al inicio del string
# Hacemos match contra el nombre de Kenneth Love
print(data)
print(re.match(r'Love', data)) # returns match object
print(re.match(r'Kenneth', data)) # returns None

# Search busca en todas partes la primera ocurrencia
print(re.search(r'Kenneth', data)) # returns Match object