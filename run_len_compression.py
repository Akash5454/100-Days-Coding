"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Time Complexity O(n)
"""

def compression(s1):
    index = 0
    compress_str = ""
    while index < len(s1)-1:
        count = 1
        i = index
        while i<len(s1)-1 and s1[i] == s1[i+1]:
            count += 1
            i += 1
        compress_str += s1[index] + str(count)
        index = i+1
    return compress_str 
