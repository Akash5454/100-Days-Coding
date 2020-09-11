'''

One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

Time Complexity O(n)
'''

def oneWay(string1, string2):
    if len(string1) == len(string2):
        return replaceChar(string1,string2)
    elif len(string1)+1 == len(string2):
        return insertChar(string1, string2)
    elif len(string1)-1 == len(string2):
        return insertChar(string2, string1)
    else:
        return False

def replaceChar(s1, s2):
    flag = 0
    for i,j in zip(s1,s2):
        if i != j:
            if flag == 1:
                return False
            flag = 1
    return True

def insertChar(s1,s2):
    flag = 0
    i,j = 0, 0
    n, m = len(s1), len(s2)
    while i<n and j<m:
        if s1[i] != s2[j]:
            if flag:
                return False
            flag = 1
            j += 1
        else:
            i += 1
            j += 1
    return True        
            
            
            
