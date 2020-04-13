#Given a list of n numbers, determine if it contains any duplicate numbers.

def listDuplicates(list):
    list = [12, 5, 14, 21, 8, 24, 32]
	dict = { }

	for i in list:
		if list[i] in dict:
			return true
		else:
			dict[list[i]] += 1

	return false

#print(listDuplicates())

#Find the longest substring of unique letters in a given string of n letters.

x = "abccdeffgaabdklmopgreat"

sub = x[0]

long = sub, i

for i in sub:
    if len(sub[i] <= len(i)):
        sub += i
    print(sub
    )
