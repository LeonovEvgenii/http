#!usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading
from time import sleep
from requests import get
from requests.exceptions import ConnectionError 
from sys import argv
#import mymodule #собственный модуль
from random import randint
from generate_data import get_data


class HttpProcessor(BaseHTTPRequestHandler):
		
	def send_text(self):
		self.send_response(200)
		self.send_header('content-type', 'text/html')
		self.end_headers()
		self.wfile.write(bytes("hello", 'utf-8'))

	def send_json(self):
		self.send_response(200)
		self.send_header('content-type', 'application/json')
		self.end_headers()
		#_ = json.dumps(json.load(open(str(argv[2]), 'r')), ensure_ascii = 0, indent = 4)
		_ = json.dumps(get_data(), ensure_ascii = 0, indent = 4)
		_ = str.encode(_)
		self.wfile.write(_)

	def do_GET(self):
		self.send_json()

		
def clock_get():
	hosts = ("localhost:8080", "localhost:8081")
	while 1:
		host = hosts[randint(0, len(hosts)-1)]
		print(host)
		item_client = json.load(open(str(argv[2]), 'r'))

		print("До обновления ", argv[2], item_client)

		try:
			answer = json.loads(get("http://%s" % host).content.decode())
			item_client.update(answer)
		except ConnectionError:
			pass
		
		json.dump(item_client, open(str(argv[2]), 'w'))
		print("После обновления", item_client)
		sleep(1)

if __name__ == '__main__':
	# argv = mymodule.get_argv()

	t = threading.Thread(target=clock_get)
	t.daemon = True #выполняться непрерывно
	t.start()

	try:
		serv = HTTPServer(("localhost", int(argv[1])), HttpProcessor)
		serv.serve_forever()
	except (KeyboardInterrupt):#завершение работы сервера
		pass
	except OSError:
		print("Address already in use")