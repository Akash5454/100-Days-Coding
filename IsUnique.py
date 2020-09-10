#Is Unique: Implement an algorithm to determine if a string has all unique characters.

"""
Method 1

Time Complexity is O(n2)
"""
def isUnique(string):
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if string[i] == string[j]:
                return False
    return True

"""
Method 2

Time Complexity O(nlog(n))
"""

def isUnique(string):
    string = sorted(string)
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

"""
Method 3

Time Complexity O(n)
"""

def isUnique(string):
    d = {}
    for ch in string:
        if ch not in d.keys():
            d[ch] = 1
        else:
            return False
    return True

"""
Method 4

Time Complexity O(n)
"""

def isUnique(string):
    bool_arr = [False]*256
    for i in range(len(string)):
        if bool_arr[ord(string[i])] == True:
            return False
        else:
            bool_arr[ord(string[i])] = True
    return True        
