
'''Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word (last word means the 
last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.'''

def LastWordLength(letter): 
	word = 0

	# The last string in the set is the final output and can't be changed
    # we need to split the letters to find the 
    # I can assume there are no integers 
    # every time there is a space after the string we can continue past it
    # if there are no spaces in the string then we can start cointing the number of letters in the string
    # Best way to solve it is linear
	alpha = letter.strip() 

	for i in range(len(alpha)): 
		if alpha[i] == " ": 
			word = 0
		else: 
			word += 1
	return word

# Driver code 
if __name__ == "__main__": 
	wordset = "When they say how ya doin you say you are supercalifragilisticexpialidocious"
	print("The length of last word is", 
				LastWordLength(wordset)) 


