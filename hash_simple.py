# -*- coding: utf-8 -*-

# encode() 		: convertir string a bytes.
# hexdigest() 	: retorna la inforamción en formato hexadecimal.

import sys
import hashlib

text = 'Texto de prueba'
result = hashlib.sha1(text.encode())
print('{} HASH={}'.format(text, result.hexdigest()))


## Hash file

try:
	content = None
	with open('hash_this_file.txt', 'rb') as file:
		content = file.read()
except Exception as e:
	print('Ha ocurrido un error al abrir el archivo: {}'.format(e))
	sys.exit(0)

## Equivalente: sha1sum <filename>
result = hashlib.sha1(content)
print('HASH del archivo: {}'.format(result.hexdigest()))
