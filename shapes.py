#!usr/local/bin/python3.6
import math

class Square:
	'''Shape Class Square containing method
	   - getSurfaceArea()
	   - getType() '''
	def __init__(self):
		self.length = 0	
	def getSurfaceArea(self):
		areaSquare = self.length **2
		return areaSquare
	

class Circle:
	'''Shape Class Circle containing method
	   - getSurfaceArea()
	   - getType() '''
	def __init__(self):
		self.radius = 0	
	def getSurfaceArea(self):
		areaCircle = (self.radius**2)*math.pi
		return areaCircle


def surfaceAreaOfObject(lengthSquare, radiusCircle):
	''' Print a method surfaceAreaOfObject() outside the classes that accept an objects, and prints a message using the data from those 2 functions'''
	mysquare = Square()
	mysquare.length = lengthSquare
	mycircle = Circle()
	mycircle.radius = radiusCircle

	print('The area of the square of', lengthSquare, 'is ', mysquare.getSurfaceArea())
	print('The area of the circle of', radiusCircle, 'is ', mycircle.getSurfaceArea())


