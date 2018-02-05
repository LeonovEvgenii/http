from random import randint
from parent import Parent

class Calculate_route(Parent):

	def __init__(self):
		self.route = {"11, 22":"point1", "33, 44":"point2"}

	def get(self):
		return self.route

	def __call__(self):
		self.calc_route()

	def calc_route(self):
		number_1 = 0
		number_2 = 0
		point = 0
		s = str(number_1) + ", " + str(number_2)
		_dict = {s:"point_"+str(point)}
		n = randint(1,3)
		j = 1
		while j < n:
			number_1 += randint(1,32)
			number_2 += randint(1,32)
			point = j
			s = str(number_1) + ", " + str(number_2)
			temp =  {s:"point_"+str(point)}
			_dict.update(temp)
			j += 1
		self.route = _dict



if __name__ == '__main__':
	a = Calculate_route()
	a.calc_route()
	print(a.get_route())