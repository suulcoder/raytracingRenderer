from lib import *
from sphere import *

class Cube(object):
  def __init__(self, _min, _max, material):
    self.min = _min
    self.max = _max
    self.material = material

  def ray_intersect(self, orig, direc):
    tmin = (self.min.x - orig.x) / direc.x 
    tmax = (self.max.x - orig.x) / direc.x 
 
    if (tmin > tmax):
      tmin, tmax = tmax, tmin 
 
    if(direc.y==0):
      return None

    tymin = (self.min.y - orig.y) / direc.y 
    tymax = (self.max.y - orig.y) / direc.y 
 
    if (tymin > tymax):
      tymin, tymax = tymax, tymin 
 
    if ((tmin > tymax) or (tymin > tmax)):
      return None; 
 
    if (tymin > tmin):
      tmin = tymin; 
 
    if (tymax < tmax):
      tmax = tymax; 
 
    tzmin = (self.min.z - orig.z) / direc.z 
    tzmax = (self.max.z - orig.z) / direc.z 
 
    if (tzmin > tzmax):
      tzmin, tzmax = tzmax, tzmin 
 
    if ((tmin > tzmax) or (tzmin > tmax)):
      return None; 
 
    if (tzmin > tmin):
      tmin = tzmin; 
 
    if (tzmax < tmax):
      tmax = tzmax;

    hit = sum(orig, mul(direc, tmin))
    normal = norm(sub(hit, sub(self.max,self.min)))

    return Intersect(
      distance=tmax,
      point=hit,
      normal=normal
    )
