def alternade(s, degree):
	'''this function turns a words 
	S, into his alternates, and the
	argument degree, decides wheter every
	second, third, etc.. letter is taken'''
	t = ()
	if len(s) > 4 and degree == 2:
		a = s[0:len(s):2]
		b = s[1:len(s):2]
		c = s[2:len(s):2]
	if len(s) > 4 and degree == 3:
		a = s[0:len(s):3]
		b = s[1:len(s):3]
		c = s[2:len(s):3]
	return t + (a, b, c)
	
#--------------------------------------
print(alternade('schooled', 2))
		