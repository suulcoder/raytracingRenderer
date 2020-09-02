"""
---------------------------------------------------------------------

Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
Raytracer
Render Class: This class is an BMP image renderer
---------------------------------------------------------------------
"""

from mathModule import *
from encoder import *
from math import pi, tan
from colorModule import BLACK, WHITE, color

class Raytracer(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.current_color = WHITE
    self.clear()

  def clear(self,texture=None):
    self.pixels = [
      [BLACK for x in range(self.width)] 
      for y in range(self.height)
    ]

  def write(self, filename):
    f = open(filename, 'bw')

    # File header (14 bytes)
    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14 + 40 + self.width * self.height * 3))
    f.write(dword(0))
    f.write(dword(14 + 40))

    # Image header (40 bytes)
    f.write(dword(40))
    f.write(dword(self.width))
    f.write(dword(self.height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(self.width * self.height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    # Pixel data (width x height x 3 pixels)
    for x in range(self.height):
      for y in range(self.width):
        f.write(self.pixels[x][y])

    f.close()

  def display(self, filename='out.bmp'):
    """
    Displays the image, a external library (wand) is used, but only for convenience during development
    """
    self.write(filename)

    try:
      from wand.image import Image
      from wand.display import display

      with Image(filename=filename) as image:
        display(image)
    except ImportError:
      pass  # do nothing if no wand is installed

  def set_color(self, color):
    self.current_color = color

  def point(self, x, y, color = None):
    # 0,0 was intentionally left in the bottom left corner to mimic opengl
    try:
      self.pixels[y][x] = color or self.current_color
    except:
      # To avoid index out of range exceptions
      pass

  def scene_intersect(self,orig,direction):
  	for obj in self.scene:
  		if obj.ray_intersect(orig,direction):
  			return obj.material
  	return None

  def cast_ray(self,orig,direction):
  	impacted = self.scene_intersect(orig,direction)
  	if impacted:
  		return impacted.diffuse
  	return color(0,0,0)

  def render(self):
  	fov = pi/2
  	for y in range(self.height):
  		for x in range(self.width):
  			i = (2 * (x + 0.5)/self.width - 1) * self.width/self.height * tan(fov/2)
  			j = (1 - 2 * (y + 0.5)/self.height) * tan(fov/2)
  			direction = norm(V3(i,j,-1))
  			self.point(x,y,self.cast_ray(V3(0,0,0),direction))
