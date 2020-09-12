"""
---------------------------------------------------------------------
Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
Main: raytracing
---------------------------------------------------------------------
"""

from raytracer import Raytracer
from sphere import *
from materials import *
from mathModule import V3
from light import Light

r = Raytracer(500, 500)

r.light = Light(
  position=V3(30, 15, 50),
  intensity=1.1
)

r.background_color = color(220, 220, 220)

r.scene = [
  Sphere(V3(3.2, -1.3, -15), 2, rubber),
  Sphere(V3(4.9, 0, -14.5), 1.1, brown_skin),
  Sphere(V3(1.5, 0, -14.5), 1.1, brown_skin),
  Sphere(V3(4.3, -2.6, -14.1), 1.1, brown_skin),
  Sphere(V3(1.9, -2.6, -14.1), 1.1, brown_skin),
  Sphere(V3(3.2, 1.6, -14.9), 1.7, brown_skin),
  Sphere(V3(4.2, 2.7, -14.4), 0.7, brown_skin_detail),
  Sphere(V3(2.2, 2.7, -14.4), 0.7, brown_skin_detail),
  Sphere(V3(3.2, 1.3, -13.52), 0.6, brown_skin_detail),
  Sphere(V3(2.8, 2.1, -13.5), 0.2, eye),
  Sphere(V3(3.6, 2.1, -13.5), 0.2, eye),
  Sphere(V3(3.6, 2.1, -13.1), 0.15, eye),
  Sphere(V3(-3.2, -1.3, -15), 2, white_skin),
  Sphere(V3(-1.5, 0, -14.5), 1.1, white_skin),
  Sphere(V3(-4.9, 0, -14.5), 1.1, white_skin),
  Sphere(V3(-2.1, -2.6, -14.1), 1.1, white_skin),
  Sphere(V3(-4.5, -2.6, -14.1), 1.1, white_skin),
  Sphere(V3(-3.2, 1.6, -14.9), 1.7, white_skin),
  Sphere(V3(-2.2, 2.7, -14.4), 0.7, white_skin),
  Sphere(V3(-4.2, 2.7, -14.4), 0.7, white_skin),
  Sphere(V3(-3.2, 1.3, -13.3), 0.2, white_skin),
  Sphere(V3(-3.6, 2.1, -13.5), 0.2, eye),
  Sphere(V3(-2.8, 2.1, -13.5), 0.2, eye),
]
r.render()
r.write('out.bmp')