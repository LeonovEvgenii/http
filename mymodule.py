#!usr/bin/python3
from sys import argv

def help():
	print("\nВведены значения по умолчанию 8080 и 1.json. Нужно вводить порт и файл.\n")

def get_argv():
	port = '8080'
	file_name = 'c1.json'	
	try:
		port, client_file_name, server_file_name = argv[1], argv[2], argv[3]
	except IndexError:
		help()
	return port, client_file_name, server_file_name


if __name__ == '__main__':
	argv = get_argv()	
	print (argv)
