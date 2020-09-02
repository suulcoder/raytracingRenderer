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

out = 'out.bmp'
r = Raytracer(3000, 3000)


#Snowman:
r.scene = [
	Sphere(V3(0.2,-5,-8),0.12,gray_teeth),
	Sphere(V3(-0.2,-5,-8),0.12,gray_teeth),
	Sphere(V3(0.6,-5.1,-8),0.12,gray_teeth),
	Sphere(V3(-0.6,-5.1,-8),0.12,gray_teeth),
	Sphere(V3(0.5,-6.8,-8),0.12,black_botton),
	Sphere(V3(-0.5,-6.8,-8),0.12,black_botton),
	Sphere(V3(0.5,-6.7,-8),0.25,snow),
	Sphere(V3(-0.5,-6.7,-8),0.25,snow),
	Sphere(V3(0.5,-6.7,-8),0.3,black_botton),
	Sphere(V3(-0.5,-6.7,-8),0.3,black_botton),
	Sphere(V3(0,-5.8,-8),0.4,carrot),
	Sphere(V3(0,3,-8),0.9,black_botton),
	Sphere(V3(0,0,-8),0.7,black_botton),
	Sphere(V3(0,-2.7,-8),0.5,black_botton),	
	Sphere(V3(0,-5.8,-8),1.4,snow),
	Sphere(V3(0,-2,-8),2.3,snow),
	Sphere(V3(0,3,-8),3.3,snow),
]


r.render()
r.display(out)
