#Given a list of n numbers, determine if it contains any duplicate numbers.

def listDuplicates(list):
    list = [12, 5, 14, 21, 8, 24, 32]
    dict = {} #brackets needed to be closer together

    for i in list:
        if list[i] in dict:
            return True #capitalizing true
        else:
            dict[list[i]] += 1
    return False # capitalizing here too

print(listDuplicates(list)) #function needed to be called

#Find the longest substring of unique letters in a given string of n letters.

x = "abccdeffgaabdklmopgreat"

sub = x[0]

long, length = sub, 1 #needed to add length to problem

for i in sub:
    if len(sub[-1]) <= len(i):
        sub += i
    print(sub) #parenthesis needed to be put closer together

def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("GoldFinger"))

def recursive_is_palindrome(text, left, right):

    if left == right or left > right:
        return True
    if text[left] != text[right]:
        return False

    return recursive_is_palindrome(text, left + 1, right -1)

print(recursive_is_palindrome("tacocat", 0, len("tacocat") - 1))