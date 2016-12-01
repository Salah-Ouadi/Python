from exturtle import *
from follow import follow

def sierpinski(S):
	'''This function rewrites the string
	S, according to the SRS:
	E = FLELF and F = ERFRE'''
	#this function uses the same algorithm
	#of the algae function, which means it 
	#converts the string given into a list
	#and rewrites it following the rules given
	S = list(S)
	for i in range(len(S)):
		if S[i] == 'E':
			S[i] = 'FLELF'
		if S[i] == 'F':
			S[i] = 'ERFRE'
	return ''.join(S)
def n_sierpinski(S, n):
	'''This function create n rewriting
	of the string S according to the
	Heighway dragon rules''' 
	for i in range(n):        #for n times rewrite n
		sierpinski(S)
		S = sierpinski(S)     #each time S is equal to the last string returned
	return S
	
if __name__ == '__main__':         #execute as program
	t = Turtle()
	S = n_sierpinski('E', 8)
	
follow(t, S, 2, 60)


mainloop()
	