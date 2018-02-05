from random import randint
from parent import Parent

class Computer_vision(Parent):

	def __init__(self):
		self.objects = {"11, 22":"object1", "33, 44":"object2"}

	def get(self):
		return self.objects

	def __call__(self):
		self.recognize_objects()

	def recognize_objects(self):
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
		self.objects = _dict



if __name__ == '__main__':
	a = Computer_vision()
	a.recognize_objects()
	print(a.get_objects())