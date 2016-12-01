from exturtle import *
from follow import follow                   #import the function follow to convert the string into drawing


def dragon(S):
	'''This function rewrites the string
	S, according to the Heighway dragon
	SRS'''
	#this function uses the same algorithm
	#of the algae function, which means it 
	#converts the string given into a list
	#and rewrites it following the rules given
	S = list(S)                             
	for i in range(len(S)):
		if S[i] == 'A':
			S[i] = 'ARBF'
		if S[i] == 'B':
			S[i] = 'FALB'
	return ''.join(S)
def n_dragon(S, n):
	'''This function create n rewriting
	of the string S according to the
	Heighway dragon rules'''
	for i in range(n):         #for n times rewrite S
		dragon(S)
		S = dragon(S)          #each time S is equal to the last string 
	return S
if __name__ == '__main__':     #execute as program
	t = Turtle()
	S = n_dragon('FA', 12)

follow(t, S, 5, 90) 


	 
mainloop()