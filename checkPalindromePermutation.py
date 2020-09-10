"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)

Time Complexity O(n)
"""

def checkPalindromePermutation(string):
    count = [0]*256
    string = string.replace(" ", "").lower()
    for i in range(len(string)):
        count[ord(string[i])] += 1
    flag = 0
    for i in count:
        if i%2 != 0:
            if flag == 1:
                return False
            else:
                flag = 1
    return True            
        
