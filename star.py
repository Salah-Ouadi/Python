from TurtleWorld import *            
world = TurtleWorld()
world.delay = 0 #make the drawing more fast
t = Turtle()
print(t)
from math import cos, sin, pi  #import math elements from math module
def star(turtle, points, R, r): 
    A = (2*pi)/points
    for n in range (points):
        pu(t)                                            #no drawing when moving
        goto(t,(r*cos((n-0.5)*A)),(r*sin((n-0.5)*A)))    #coordinates on the clockwise side of P
        pd(t)                                            #drawing when moving
        goto(t,(R*cos(A*n)),(R*sin(A*n)))                #coordinates of P
        goto(t,(r*cos((n+0.5)*A)),(r*sin((n+0.5)*A)))    #coordinates on th anti-clockwise side of P 
        pd(t)
        
def starA(turtle, points, R, r): 
    A = (2*pi)/points
    for n in range (points):
        pu(t)                                            #no drawing when moving
        goto(t,(r*cos((n-0.5)*A))+150,(r*sin((n-0.5)*A)))    #coordinates on the clockwise side of P
        pd(t)                                            #drawing when moving
        goto(t,(R*cos(A*n)+150),(R*sin(A*n)))                #coordinates of P
        goto(t,(r*cos((n+0.5)*A)+150),(r*sin((n+0.5)*A)))    #coordinates on th anti-clockwise side of P 
        pd(t)

def starB(turtle, points, R, r): 
    A = (2*pi)/points
    for n in range (points):
        pu(t)                                            #no drawing when moving
        goto(t,(r*cos((n-0.5)*A)+300),(r*sin((n-0.5)*A)))    #coordinates on the clockwise side of P
        pd(t)                                            #drawing when moving
        goto(t,(R*cos(A*n)+300),(R*sin(A*n)))                #coordinates of P
        goto(t,(r*cos((n+0.5)*A)+300),(r*sin((n+0.5)*A)))    #coordinates on th anti-clockwise side of P 
        pd(t)

def starC(turtle, points, R, r): 
    A = (2*pi)/points
    for n in range (points):
        pu(t)                                            #no drawing when moving
        goto(t,(r*cos((n-0.5)*A)+450),(r*sin((n-0.5)*A)))    #coordinates on the clockwise side of P
        pd(t)                                            #drawing when moving
        goto(t,(R*cos(A*n)+450),(R*sin(A*n)))                #coordinates of P
        goto(t,(r*cos((n+0.5)*A)+450),(r*sin((n+0.5)*A)))    #coordinates on th anti-clockwise side of P 
        pd(t)
star(t, 5, 50, 20)
starA(t, 6, 50, 20)
starB(t, 7, 50, 20)
starC(t, 8, 50, 20)
       
    

        



wait_for_user()
    