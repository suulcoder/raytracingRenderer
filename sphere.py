from mathModule import sub,dot, length
from math import sqrt

class Sphere(object):
	def __init__(self, center, r, material):
		self.center = center
		self.r = r
		self.material = material
	
	def ray_intersect(self,orig,direction):
		L = sub(self.center,orig)
		tca = dot(L,direction)
		d2 = length(L)**2 - tca**2
		if d2 > self.r**2:
			return False
		thc = (self.r**2 - d2)**(1/2)
		t0 = tca - thc
		t1 = tca + thc

		if t0<0:
			t0 = t1
		if t1<0:
			return False

		return True	