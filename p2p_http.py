#!usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading
from time import sleep
from requests import get
from sys import argv
import mymodule #собственный модуль

item_client = {"111":111}
item_server = {"222":222}

class HttpProcessor(BaseHTTPRequestHandler):

	def extract_content(self):
		with open('s1.json', 'r') as file:
			content = file.read()
		return content
		
	def send_text(self):
		self.send_response(200)
		self.send_header('content-type', 'text/html')
		self.end_headers()
		self.wfile.write(bytes("hello", 'utf-8'))

	def send_json(self):
		content = self.extract_content()
		print(content)
		self.send_response(200)
		self.send_header('content-type', 'application/json')
		self.end_headers()
		_ = json.dumps(item_server, ensure_ascii = 0, indent = 4)
		_ = str.encode(_)
		self.wfile.write(_)

	def open_file(self):
		pass

	def do_GET(self):
		self.send_json()
		
		
def clock_get():
	#list_port = (8080)
    while True:
        #print(get("http://localhost:8080").content.decode())
        #_url = "http://localhost:"
        #for i in list_port
        #	url = _url + i
        answer = eval(get("http://localhost:8080").content.decode())
        item_client.update(answer)
        print(item_client)
        sleep(1)

if __name__ == '__main__':
	argv = mymodule.get_argv()

	t = threading.Thread(target=clock_get)
	t.daemon = True #выполняться непрерывно
	t.start()

	try:
		serv = HTTPServer(("localhost", int(argv[0])), HttpProcessor)
		serv.serve_forever()
	except (KeyboardInterrupt):#завершение работы сервера
		pass
	except OSError:
		print("Address already in use")