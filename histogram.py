from sys import argv, exit


def histogram(x, percentage):
	'''This function draws a simple histogram of 
	the percentages, in the list percentage, versus
	the numbers in range(x)'''
	P = percentage    
	for i in range(x):
		if P[i] != 0:    
			print(i, '*'*int(P[i]),'   ',P[i])  
		
		
def histogram_length(L):
	'''Given a list of strings L, return a list 
	of integers,H, where H[i] is the number of
	times that strings of length i occurred in L'''
	H = [0]*21     #create a list for counting number of times length i occurs in L
	for i in L:
		if len(i) > 0:     #if length i > 0, go to list H, look for index
			H[len(i)] += 1 #with same value of length(i), and add 1 each time.
	return H
	
if __name__ == '__main__':             #execute as program  
	file = open('dracula.txt', 'r')    #open file
	words = []						   #create an empty list 'words'
	line = file.readline()             #read one line at atime 
	while len(line) > 0:
		words.append(line.strip())     #call the strip method of the string object
		line = file.readline()	       #and add item to the list words
	t = histogram_length(words)        #return list for words length count in dracula.txt
	P = []                             #create an empty list for percentages
	for i in t:
		i = round( i / len(words)*100, 3)    #convert counters in t to percentages
		P.append(i)                          #and add them to the list P. 
	print('Histogram of the percentages of times that words of different lengths occur in dracula.txt:')
	print()
	x = histogram(21, P)     
	
		
