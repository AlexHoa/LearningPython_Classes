#!usr/local/bin/python3.6

class Point:
	'''Point Class containing an x and a y variable:
	implement __str__ so it prints something like Point(33,42)
	move method accepting x and y to move it by
	method that takes another Point and calulates the distance between those in x and y '''
	def __init__(self,x = 0,y =0):
		self.x = x
		self.y = y

	def __str__(self):
		return "Point(%d, %d)"%(self.x, self.y)
	
	def distance(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return print(dx, dy)

