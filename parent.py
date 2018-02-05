class Parent(object):
	
	def __str__(self):
		return self.__class__.__name__


if __name__ == '__main__':
	a = Parent()
	print(a.__str__())