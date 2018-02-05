from random import randint
from parent import Parent

class Expert_system(Parent):
	
	def __init__(self):
		self.list_comand = {}

	def get(self):
		return self.list_comand

	def __call__(self):
		self.generate_command()

	def generate_command(self):
		_dict = {}
		variant = ("move", "recognize_objects", "calc_route", "recognize_items", "generate_command")
		n = randint(1,3)
		j = 0
		while j < n:
			temp =  {"command_"+str(j):str(variant[randint(0,4)])}
			_dict.update(temp)
			j += 1
		self.list_comand = _dict



if __name__ == '__main__':
	a = Expert_system()
	a.generate_command()
	print(a.get_comands())