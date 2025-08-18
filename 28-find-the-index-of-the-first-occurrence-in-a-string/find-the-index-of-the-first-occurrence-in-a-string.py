class Solution(object):
    def strStr(self, haystack, needle):
       a,b=len(haystack),len(needle)

       if b == 0:
        return 0

       for c in range(a-b+1):
        if haystack[c:c+b] == needle:
            return c
       return -1      
        