from shuffle import *
from histogram import histogram
def add_to_11(visible):
	'''take as argument the list of visible
	cards and returns tuples of indices indicating
	which cards adds to eleven'''
	v = visible
	t = tuple()                              #create empty tuple 
	for i in range(len(v)):                   #iterate over the list twice so
		for e in range(len(v)):				  #that our function check each
			if v[i] + v[e] == 11:             #element in the list, if pair add to eleven 
				return t + (v[i], v[e])       #return tuple with cards that add to eleven,
	if len(t) == 0:                           #if tuple is empty so no cards add to eleven'
		return t                              #return empty tuple.
				
def jqk(visible):
	'''take as argument the list of visible
	cards and return tuple of indices indicating
	which cards are Jack, Queen and King'''
	v = visible
	t = tuple() 
	for i in range(len(v)):                                   #This function works as the add_to_11 one
		for e in range(len(v)):                               #but it checks if Jack, Queen and King are
			for a in range(len(v)):                           #in the visible list, if they are the function
				if v[i] == 11:                                #return a tuple with Jack, Queen and King in it,
					if v[e] == 12:                            #if those three cards are not in the list visible
						if v[a] == 13:                        #return an empty tuple.
							return  t + (v[i], v[e], v[a])
	if len(t) == 0:
		return t

def play(deck, verbose):
	'''This function plays a single
	game of patience with a deck deck,
	The Booloean argument verbose controls
	whether the visible cards are printed
	at each stage of the game; if verbose
	is False, the progress of the game is 
	not printed'''
	deck = shuffle(deck)                                  
	visible = []                                   #create an empty list for visible cards
	visible += deck[:2]							   #place face up the first two cards of the shuffled deck
	del deck[:2]                                   #remove those cards from the deck
	while len(deck) != 0 and len(visible) <= 9:    #while cards in the deck and we have less or 9 piles of visible cards play game 
		if verbose == True:                        
			for i in visible:                       
				print(i,end=' ')                   #print cards in horizontal and in
			print()                                #a new line each time
		t = jqk(visible)                           #check that Jack, Queen and King not in 
		if len(t) > 0:                             #visible, if they are:
			for i in t:
				c = visible.index(i)               #find the index of Jack, Queen and King
				del visible[c]                     #in the list visible, and delete them
			visible += deck[:3]                    #take three new cards from the deck
			del deck[:3]                           #remove three cards from the deck
		x = add_to_11(visible)                     #check that cards don't add to eleven
		if sum(x) == 11:                           #if they do add to eleven: 
			for i in x:                            
				d = visible.index(i)               #found the index of the cards in the 
				del visible[d]                     #list visible and delete them.
			visible += deck[:2]					   #take two new cards from the deck
			del deck[:2]                           #remove two cards from the deck
		if len(x) == 0:                            #if function add_to_11 return an empty tuple
			visible += deck[:1]                    #draw a new card from the deck
			del deck[:1]                           #remove one card from the deck
	return len(deck)
	
def many_plays(N):
		'''This function plays N games of
		patience, and return a list of length
		53 showing the number of times that
		games ended with 0,..'52'''
		remaining = [0]*53                           #create a list for counting how many cards 
		for i in range(N):                           #are left in the deck after each game
			t = play(list(range(1, 14))*4, False)    #play patience for N times
			remaining[t] += 1
		return remaining                             
if __name__ == '__main__':
	b = play(list(range(1, 14))*4, True)
	if b > 0:
		print('Players Loses', b, 'cards left in the deck')
	else:
		print('Players Wins', b, 'cards left in the deck')
	remaining = many_plays(10000)                         
	P = []
	for i in remaining:                               #change remaining integers into percentages
		i = round(i / 10000* 100, 4)
		P.append(i)

	x = histogram(53, P)
	print('This is the histogram of the percentage of times that games ended with n cards left in the deck')