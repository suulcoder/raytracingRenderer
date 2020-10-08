from lib import *
from sphere import *
from math import pi, acos, atan2
import png, array

class Plane(object):
  def __init__(self, y, material):
    self.y = y
    self.material = material

  def ray_intersect(self, orig, direction):
    d = -(orig.y + self.y) / direction.y
    pt = sum(orig, mul(direction, d))

    if d <= 0 or abs(pt.x) > 2 or pt.z > -5 or pt.z < -10:
      return None

    normal = V3(0, 1, 0)

    return Intersect(
      distance=d,
      point=pt,
      normal=normal
    )

import mmap
import numpy

class Envmap(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        reader = png.Reader(filename=self.path)
        self.width, self.height, self.pixels, self.metadata = reader.read_flat()

    def get_color(self, direction):
      width = 3840
      height = 2160
      direction = norm(direction)

      x = int((atan2(direction.z, direction.x) / (2 * pi) + 0.5) * width)
      y = int(acos(-direction.y) / pi * height)
      index = (y * self.width + x) * 3 % len(self.pixels)

      processed = self.pixels[index:index+3]
      return color(processed[0], processed[1], processed[2])