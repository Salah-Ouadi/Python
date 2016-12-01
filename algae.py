def algae(S):
	'''takes a string and return the string
	rewritten according to the algae rules'''
	S = list(S)                      #convert string to a list
	for i in range(len(S)):          
		if S[i] == 'A':              #if item in S is A, change it to AB
			S[i] = 'AB'
		if S[i] == 'B':              #if item in S is B, change it to A
			S[i] = 'A'
	return ''.join(S)                #after rewriting the list convert it into a string
def algae_1(S, n):
	'''This function create n rewriting
	of the string S according to the
	algae rules'''
	for i in range(n):         #for n times rewrite S
		algae(S)
		S = algae(S)           #each time S equal to the last string returned
	return S

	

	
if __name__ == '__main__':     #execute as program 
	print('The first 10 rewritings of the algae sequence are:', algae_1('A', 10))
	C = len(algae_1('A', 30))
	print('The length of the string corresponding to 30 rewritings is:', C)
	
	
	


	
