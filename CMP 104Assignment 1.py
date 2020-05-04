# -*- coding: utf-8 -*-
"""
Spyder Editor

This is" a temporary scr"ipt file.

"""
"""
def calcArea(length_a ):
    A = length_a**2
    return A
length_a = float(input("Enter the length of the square: ")) 

A = calcArea(length_a)
print(A)

def calcAreaRectangle(length_l, breadth_b):
    A = length_l*breadth_b
    return A
length_l = float(input("Enter the length of the rectangle: "))
breadth_b = float(input("Enter the breadth of the rectangle: "))

A = calcAreaRectangle(length_l, breadth_b)
print(A)

def calcAreaOfTriangle(base_b, height_h):
    A = 1/2*base_b*height_h
    return A
base_b = float(input("Enter the base of the triangle: "))
height_h = float(input("Enter the height of the triangle: "))

A = calcAreaOfTriangle(base_b, height_h)
print(A)


def calcAreaOfTrapezoid(b1, b2, height):
    A = 1/2*(b1+b2)*height
    return A
b1 = float(input("Enter the first base of the trapezium: "))
b2 = float(input("Enter the second base of the trapezium: "))
height = float(input("Enter the height of the trapezium: "))

A = calcAreaOfTrapezoid(b1, b2, height)
print(A)
 
 
def calcAreaOfCircle(radius):
    A = 22/7*radius**2
    return A
radius = float(input("Enter the radius: "))

A = calcAreaOfCircle(radius)
print(A)


def calcCircumferenceOfCircle(radius):
    A = 2*22/7*radius
    return A
radius = float(input("Enter the radius: "))

A = calcCircumferenceOfCircle(radius)
print(A)


def calcSurfaceAreaOfACube(length_a):
    S = 6*length_a**2
    return S
length_a = float(input("Enter the length of the side of the cube: "))

S = calcSurfaceAreaOfACube(length_a)
print(S)


def calcCurvedSurfaceArea(radius, height):
    A = 2*22/7*radius*height
    return A
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

A = calcCurvedSurfaceArea(radius, height)
print(A)


def calcTotalSurfaceArea(radius, height):
    summ = radius + height
    A = 2*22/7*radius*summ
    return A
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

A = calcTotalSurfaceArea(radius, height)
print(A) 


def calcVolumeOfCylinder(radius, height):
    V = 22/7*radius**2*height
    return V
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

V = calcVolumeOfCylinder(radius, height)
print(V)


def calcAcceleration(velocity_v, initialvelocity_u, time_t):
    a = velocity_v-initialvelocity_u/time_t
    return a
velocity_v = float(input("Enter the final velocity in metres: "))
initialvelocity_u = float(input("Enter the initial velocity in metres: "))
time_t = float(input("Enter the time taken in seconds: "))

a = calcAcceleration(velocity_v, initialvelocity_u, time_t)
print(a)


def calcDensity(mass, volume):
    p = mass/volume
    return p
mass = float(input("Enter the mass in grams: "))
volume = float(input("Enter the volume in centimetre cube: "))

p = calcDensity(mass, volume)
print(p)


def calcPressure(force, area):
    P = force/area
    return P
force = float(input("Enter the force: "))
area = float(input("Enter the area: "))

P = calcPressure(force, area)
print(P)

def calcKineticEnergy(mass, volume):
    E = 1/2*mass*volume**2
    return E
mass = float(input("Enter the mass: "))
volume = float(input("Enter the volume: "))

E = calcKineticEnergy(mass, volume)
print(E)
"""
def calcVoltaage(current_I, resistance_R):
    V = current_I* resistance_R
    return V
current_I = float(input("Enter the current: "))
resistance_R = float(input("Enter the resistance in ohms: "))

V =  calcVoltaage(current_I, resistance_R)
print(V)


               
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 