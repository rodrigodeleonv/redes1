# -*- coding: utf-8 -*-

#
# Ejemplo conceptual
# FTP Client
#

import socket
from ftplib import FTP, error_perm

# Autenticación
ROUTER_username = ''
ROUTER_password = ''
host = ''	# IP addr.
SOCKET_TIMEOUT = 3		# Segundos
PORT_FTP = 21

# FTP
# NLST:	Returns a list of file names in a specified directory.
# https://en.wikipedia.org/wiki/List_of_FTP_commands

try:
	ftp = FTP(host, timeout=6)
except socket.error as e:
	print(e)

try:                
	ftp.login(ROUTER_username, ROUTER_password)
	listar_archivos = ftp.nlst()
	for file in listar_archivos:
		print('* '+file)
except error_perm, resp:
	resp = str(resp)
	if '530' in resp: # FTP Login Incorrecto
		print('¡Las credenciales son incorrectas!')
	else:
		print(resp)
		# raise
except AttributeError as e:
	print(e, host)
except socket.timeout as e:
	print('{} ftp.login timeout'.format(e), host)

# Cerrando conexión FTP
try:
	ftp.quit()
except Exception as e:
	pass
print('Conexion FTP cerrada')

