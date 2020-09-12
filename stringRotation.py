"""
String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

Time Complexity O(n+m)
"""
    
def rotateString(A, B):
    if len(A) != len(B): return False
    if len(A) == 0: return True
    
    # capture length of strings
    # then make both strings 1 indexed
    N = len(A)
    A = " " + A + A
    B = " " + B
    
    # calculate pi table, it captures the length of the
	# longest prefix that is also the suffix
    pi = [0] * (N+1)
    left, pi[0] = -1, -1
    for right in range(1, N+1):
        while left >= 0 and B[left + 1] != B[right]:
            left = pi[left]
        left += 1
        pi[right] = left
    
    # do matching
    j = 0
    for i in range(1, (2*N)+1):
        while j >= 0 and B[j+1] != A[i]:
            j = pi[j]
        j += 1
        if j == N: return True
    
    return False            
    
