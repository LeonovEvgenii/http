from random import randint
from parent import Parent

class Geoinformation_system(Parent):

	def __init__(self):
		self.items = {"11, 22":"item1", "33, 44":"item2"}

	def get(self):
		return self.items

	def __call__(self):
		self.recognize_items()

	def recognize_items(self):
		_dict = {}
		list_name = ['q', 'w', 'e', 'r', 't', 'y']
		n = randint(1,3)
		j = 0
		while j < n:
			i = 0
			name = ""
			while i<7:
				name += str(list_name[randint(0,5)])
				i += 1
			s = str(randint(1,99)) + ", " + str(randint(1,99))
			temp = {s:name}
			_dict.update(temp)
			j += 1
		self.items = _dict


if __name__ == '__main__':
	a = Geoinformation_system()
	a.recognize_items()
	print(a.get_items())