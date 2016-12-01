from random import random
def shuffle(L):
	'''This function uses the Durstenfeld 
	algorithm to shuffle the list L'''
	A = [item for item in L] #copy the list
	for i in range(len(L)):  
		j = int(random()*i)  #random integer between 0 and length of L, to use as index value
		L[i], L[j] = L[j], L[i]	#exchange indices of items
		assert len(L) == len(A) #throw an exception if list's lengths not equal
	return L

def quality(L):
	'''This function evaluates the
	quality of the shuffle of a list'''
	previous_smaller = 0           #create a counter for fraction of times
	for i in range(len(L)):        #the second item of two adjacent items
		if L[i] > L[i-1]:          #is larger than the first
			previous_smaller += 1
	return previous_smaller/(len(L))  #return quality of shuffle

def average_quality(L, trials):
	'''This function finds the average
	quality of trials shuffles of L'''
	average = 0                   	#create a counter for the shuffle quality
	for i in range(trials):
		shuffle(L)
		quality(L)
		average += quality(L)     	#add quality to average each time
	aq = round((average/trials), 3) #average quality after n trials

	print('The average quality of', trials, 'shuffles of the list with', len(L), 'items in it, is:', aq)
	
		
if __name__ == '__main__':
	average_quality(list(range(100)), 1000)


