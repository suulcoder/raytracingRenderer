from lib import *
from sphere import *
import math

class Cylinder(object):
  def __init__(self, radius, height, center, material):
    self.radius = radius
    self.height = height
    self.center = center
    self.material = material

  def ray_intersect(self, orig, direc):
    a = (direc.x * direc.x) + (direc.z * direc.z)
    b = 2*(direc.x*(orig.x- self.center.x) + direc.z*(orig.z-self.center.z))
    c = (orig.x - self.center.x) * (orig.x - self.center.x) + (orig.z - self.center.z) * (orig.z - self.center.z) - (self.radius*self.radius)
    
    delta = b*b - 4*(a*c);
    if(abs(delta) < 0.001):
        return None; 
    if(delta < 0.0):
        return None;
    
    t1 = (-b - math.sqrt(delta))/(2*a)
    t2 = (-b + math.sqrt(delta))/(2*a)
    
    t = t1
    if (t1>t2):
        t = t2
    
    r = orig.y + t*direc.y;
    
    if ((r >= self.center.y) and (r <= self.center.y + self.height)):
        hit = sum(orig, mul(direc, t))
        normal = norm(sub(hit, self.center))
        return Intersect(
            distance=t,
            point=hit,
            normal=normal
          )

    return None


    
