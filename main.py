from ray import *
from sphere import *
from plane import *
from cube import *
from cone import *
from cilinder import *
from lib import *
import random

r = Raytracer(860, 540)

r.light = Light(
  position=V3(0, 20, 15),
  intensity=1.0
)

ballons = [
	Material(color=color(255,15,15),albedo=(0.7,10,0.8,0), spec=325),
	Material(color=color(15,255,15),albedo=(0.7,10,0.8,0), spec=325),
	Material(color=color(15,15,255),albedo=(0.7,10,0.8,0), spec=325),
	Material(color=color(255,255,15),albedo=(0.7,10,0.8,0), spec=325),
	Material(color=color(255,15,255),albedo=(0.7,10,0.8,0), spec=325),
	Material(color=color(15,255,255),albedo=(0.7,10,0.8,0), spec=325),
]

bloks = [
	Material(color=color(255,5,255), albedo=(0.9, 5, 0, 0, 0), spec=1025),
	Material(color=color(205,55,255), albedo=(0.9, 5, 0, 0, 0), spec=1025),
	Material(color=color(155,105,255), albedo=(0.9, 5, 0, 0, 0), spec=1025),
	Material(color=color(105,155,255), albedo=(0.9, 5, 0, 0, 0), spec=1025),
	Material(color=color(55,205,255), albedo=(0.9, 5, 0, 0, 0), spec=1025),
	Material(color=color(5,255,255), albedo=(0.9, 5, 0, 0, 0), spec=1025),
]

gold = Material(color=color(102, 102, 0), albedo=(0.6, 0.3, 0.1, 0), spec=50)
rubber = Material(color=color(80, 0, 0), albedo=(0.9, 0.1, 0, 0, 0), spec=100)
wood = Material(color=color(51, 25, 0), albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
leafs = Material(color=color(0, 102, 0), albedo=(0.9, 0.25, 0, 0.15, 0), spec=150)

water = Material(color=color(150, 180, 200), albedo=(0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)
pyramid = Material(color=color(102,102,0), albedo=(0.9, 5, 0, 0, 0), spec=1025),	

r.background_color = color(50, 50, 200)

r.scene = [
  
  #robot
  Cube(V3(1.5,0.95,7.5),V3(1.8,0.85,8),bloks[0]),
  Cube(V3(1.8,0.85,7.5),V3(1.7,0.75,8),bloks[1]),
  Cube(V3(1.8,0.75,7.5),V3(1.7,0.65,8),bloks[2]),
  Cube(V3(1.8,0.65,7.5),V3(1.7,0.55,8),bloks[3]),
  Cube(V3(1.8,0.55,7.5),V3(1.7,0.45,8),bloks[4]),
  Cube(V3(1.8,0.45,7.5),V3(1.7,0.35,8),bloks[5]),
  Cube(V3(2.2,0.95,7.5),V3(2.0,0.85,8),bloks[0]),
  Cube(V3(2.1,0.85,7.5),V3(2.0,0.75,8),bloks[1]),
  Cube(V3(2.1,0.75,7.5),V3(2.0,0.65,8),bloks[2]),
  Cube(V3(2.1,0.65,7.5),V3(2.0,0.55,8),bloks[3]),
  Cube(V3(2.1,0.55,7.5),V3(2.0,0.45,8),bloks[4]),
  Cube(V3(2.1,0.45,7.5),V3(2.0,0.35,8),bloks[5]),
  Cube(V3(1.7,0.35,7.5),V3(2.1,0.25,8),bloks[0]),
  Cube(V3(1.7,0.25,7.5),V3(2.1,0.15,8),bloks[1]),
  Cube(V3(1.7,0.15,7.5),V3(2.1,0.05,8),bloks[2]),
  Cube(V3(1.7,0.05,7.5),V3(2.1,-0.05,8),bloks[3]),
  Cube(V3(1.7,-0.05,7.5),V3(2.1,-0.15,8),bloks[4]),
  Cube(V3(1.7,-0.15,7.5),V3(2.1,-0.25,8),bloks[5]),
  Cube(V3(1.4,-0.25,7.5),V3(2.4,-0.35,8),bloks[0]),

  Cube(V3(2.3,0.35,7.5),V3(2.4,0.25,8),bloks[0]),
  Cube(V3(2.3,0.25,7.5),V3(2.4,0.15,8),bloks[1]),
  Cube(V3(2.3,0.15,7.5),V3(2.4,0.05,8),bloks[2]),
  Cube(V3(2.3,0.05,7.5),V3(2.4,-0.05,8),bloks[3]),
  Cube(V3(2.3,-0.05,7.5),V3(2.4,-0.15,8),bloks[4]),
  Cube(V3(2.3,-0.15,7.5),V3(2.4,-0.25,8),bloks[5]),

  Cube(V3(1.4,0.35,7.5),V3(1.5,0.25,8),bloks[0]),
  Cube(V3(1.4,0.25,7.5),V3(1.5,0.15,8),bloks[1]),
  Cube(V3(1.4,0.15,7.5),V3(1.5,0.05,8),bloks[2]),
  Cube(V3(1.4,0.05,7.5),V3(1.5,-0.05,8),bloks[3]),
  Cube(V3(1.4,-0.05,7.5),V3(1.5,-0.15,8),bloks[4]),
  Cube(V3(1.4,-0.15,7.5),V3(1.5,-0.25,8),bloks[5]),

  Cube(V3(1.80,-0.35,7.5),V3(2.00,-0.55,8),bloks[0]),

  #forest
  Cone(0.9, 1.5, V3(0,-1.15,10), leafs),
  Cylinder(0.3, 1.5, V3(0,-0.25,10), wood),

  Cone(0.9, 1.5, V3(-2,-1.15,10), leafs),
  Cylinder(0.3, 1.5, V3(-2,-0.25,10), wood),

  Cone(0.9, 1.5, V3(-3,-1.15,10), leafs),
  Cylinder(0.3, 1.5, V3(-3,-0.20,10), wood),

  Cone(0.9, 1.5, V3(-4.1,-1.05,10), leafs),
  Cylinder(0.3, 1.5, V3(-4.1,-0.15,10), wood),

  Cone(0.9, 1.5, V3(-5,-1.05,10), leafs),
  Cylinder(0.3, 1.5, V3(-5,-0.15,10), wood),
 
  Cone(0.9, 1.5, V3(-6.2,-0.97,10), leafs),
  Cylinder(0.3, 1.5, V3(-6.2,-0.10,10), wood),

  Cone(0.9, 1.5, V3(-7.3,-1.00,10), leafs),
  Cylinder(0.3, 1.5, V3(-7.3,0.02,10), wood),

  Cone(0.9, 1.5, V3(-8.3,-0.90,10), leafs),
  Cylinder(0.3, 1.5, V3(-8.3,0.10,10), wood),

  #athenas
  Cube(V3(3.30,-0.3,7),V3(5.3,-0.5,8),gold),
  Cube(V3(3.30,-0.3,7),V3(3.4,1.0,7.3),gold),
  Cube(V3(5.3,-0.3,8),V3(5.2,1.11,7.7),gold),
  Cube(V3(3.30,-0.3,8),V3(3.4,1.02,7.7),gold),	
  Cube(V3(5.3,-0.3,7),V3(5.2,1.1,7.3),gold),

  Cube(V3(3.30,-1.8,7),V3(5.3,-2.3,8),gold),
  Cube(V3(3.30,-1.8,7),V3(3.4,-0.5,7.3),gold),
  Cube(V3(5.3,-1.8,8),V3(5.2,-0.5,7.7),gold),
  Cube(V3(3.30,-1.8,8),V3(3.4,-0.5,7.7),gold),	
  Cube(V3(5.3,-1.8,7),V3(5.2,-0.5,7.3),gold),



]
x=50
y=50
for i in range(1,x):	
	for j in range(1,y):
		r.scene.append(Sphere(
		V3(4*(i-x/2)/x, 4*(j-y/2)/y, -random.randint(2,i+2)), 
			random.randint(0,10)*0.003, 
			water
		))


"""
for i in range(1,5):
	for j in range(1, 5):
		r.scene.append(Sphere(V3(((i-40)/40), ((j-20)/40)*2, -random.randint(10,i+10)), random.randint(0,i)*0.001, random.choice(ballons)))
"""
r.scene.append(Sphere(V3(-3.5, -5,3), 0.5, random.choice(ballons)))

r.envmap = Envmap('back3.png')

r.render()
r.write('out.bmp')