from random import randint
from parent import Parent

class Chassis(Parent):

	def __init__(self):
		self.speed = 0

	def __call__(self):
		self.move(5)

	def get(self):
		return self.speed

	def move(self, spd = 5):
		if spd <= 0:
			spd = 0
			return
		self.speed = randint(spd - 1, spd +5)
		

if __name__ == '__main__':
	a = Chassis()
	#a.move(-9)
	#print(a.getSpeed())
	print(a.__str__())