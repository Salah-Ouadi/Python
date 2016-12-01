from exturtle import *


def follow(t, S, step, angle):
	'''This function makes the turtle
	t, draw the path described by the
	string S.'''
	S = list(S)                   #convert string to a list
	for i in range(len(S)):    
		hideturtle(t)             #hide turtle while drawing
		if S[i] == 'F':           #if item in S is F, move forward of specified distance
			forward(t, step)
		if S[i] == 'E':           #if item in S is E, move forward of specified distance
			forward(t, step)
		if S[i] == 'L':
			left(t, angle)     	  #if item in S is L, turn left of specified angle
		if S[i] == 'R':
			right(t, angle)	      #if item in S is R, turn right of specified angle
	showturtle(t)                 #show turtle after drawing


			
#--------------------------
if __name__ == '__main__':       #execute as program
	t = Turtle()
	follow(t, ('E'*10 + 'R' + 'F'*10 + 'L' + 'E'*10 + 'R' + 'F'*10), 10, 90)     #S is random just to the test that the function works



	
	
mainloop()          #keep Python Turtle Graphics window open after drawing
			