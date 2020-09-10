#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

"""

Time Complexity O(n)

"""

def checkPermutation(string1, string2):
    count = [0]*256
    if len(string1) != len(string2):
        return False
    for i in string1:
        count[ord(i)] += 1
    for i in string2:
        if count[ord(i)] == 0:
            return False
        count[ord(i)] -= 1

    return True
