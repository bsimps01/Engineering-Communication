'''Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.'''

# Variable Table
'''
arr = ints consisting of [1, 2, 3, 1, 3, 6, 6]
size = len(arr)
abs = to help return the absolute value in the array
'''

'''Go down the array from start to end.
For every element,take its absolute value 
and if the abs(array[i])‘th element is positive, 
the element has not encountered before, 
else if negative the element has been encountered 
before print the absolute value of the current element.
'''

def repeating(arr, size): 
	
	print("The repeating elements are: ") 
	
	for i in range(0, size): 
		
		if arr[abs(arr[i])] >= 0: 
			arr[abs(arr[i])] = -arr[abs(arr[i])] 
		else: 
			print (abs(arr[i])) 
			
arr = [1, 2, 3, 1, 3, 6, 6] 
arr_size = len(arr) 

repeating(arr, arr_size) 

 
