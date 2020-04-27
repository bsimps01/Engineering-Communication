'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).'''

'''  -Find out pivot point and divide the array in two
      sub-arrays.
     -Call binary search for one of the two sub-arrays.
     -If element is greater than index element then
             search in left array
     -Else Search in right array'''

#Variable Table

'''
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
start = 4
end = 3
key = 6
mid = the start and end dvided to search 
in the arrays separated
'''

def search (arr, start, end, key): 
	if start > end: 
		return -1
	
	mid = (start + end) // 2
	if arr[mid] == key: 
		return mid 

	if arr[start] <= arr[mid]: 

#When this array is sorted we can identify the key value between the beginning half or end alternate half
		if key >= arr[start] and key <= arr[mid]: 
			return search(arr, start, mid - 1, key) 
		return search(arr, mid + 1, end, key) 

#Checks to see if the array is not sorted 
	if key >= arr[mid] and key <= arr[h]: 
		return search(a, mid+1, h, key) 
	return search(arr, l, mid-1, key) 

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 6
i = search(arr, 0, len(arr)-1, key) 
if i != -1: 
	print ("Index: %d"%i) 
else: 
	print ("Key not found") 


		
