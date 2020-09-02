from colorModule import color

class Material(object):
	def __init__(self, diffuse):
		self.diffuse = diffuse


ivory = Material(color(100,100,80))
rubber = Material(color(200,50,80))
snow = Material(color(255,255,255))
black_botton = Material(color(0,0,0))
gray_teeth = Material(color(50,50,50))
carrot = Material(color(255,128,0))