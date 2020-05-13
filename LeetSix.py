
'''You are climbing a stair case. 
It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?'''

# By using the fibonnaci approach we can try to return the number of ways we can
# find the stairs, by finding each number to reach the certain n times
# Time complexity is O(n^2) since we are doing redundant calculations
# by adding more than one time, it increases exponentially
def steps(n): 
	if n <= 1: 
		return n 
	return steps(n-1) + steps(n-2) 

# returns the number of ways to reach s'th stair 
def counts(s): 
	return steps(s + 1) 


s = 7
print("Number of ways = ") 
print(counts(s))


