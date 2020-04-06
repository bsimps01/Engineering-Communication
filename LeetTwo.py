
'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string'''

# When utilziing the most common prefix, it is going to be safe to assume that all of our words will be strings and that each of these words
# will be stored in an array. Every single time that a word or a set of words have a sequence of characters that have the longest string we can
# add them to a list.

def findMinLength(strList): 
    return len(min(arr, key = len)) # find the length of the array so that we can find the listed combination
  
def allContainsPrefix(strList, str, start, end): 
    for i in range(0, len(strList)): 
        word = strList[i] 
        for j in range(start, end + 1): 
            if word[j] != str[j]: 
                return False            # Checks the range/length of the list until they are found so we can append them to our list
    return True
  
# A Function that returns the longest 
# common prefix from the array of strings 
def CommonPrefix(strList): 
    index = findMinLength(strList) 
    prefix = ""     # Our resultant string 
  
    # We will do an in-place binary search  
    # on the first string of the array 
    # in the range 0 to index  
    low, high = 0, index - 1
    while low <= high: 
        # Same as (low + high)/2, but avoids 
        # overflow for large low and high 
        mid = int(low + (high - low) / 2) 
        if allContainsPrefix(strList, strList[0], low, mid): 
            # If all the strings in the input array  
            # contains this prefix then append this  
            # substring to our answer 
            prefix = prefix + strList[0][low:mid + 1] 
  
            # And then go for the right part  
            low = mid + 1
        else: 
            # Go for the left part  
            high = mid - 1
  
    return prefix 
  
#Creates the arrays and instantiates our functions
arr = ["boomer", "bomb","bogus", "boo"] 
lcp = CommonPrefix(arr) 
  
if len(lcp) > 0: 
    print ("The longest common prefix is " + str(lcp)) 
else: 
    print ("There is no common prefix")