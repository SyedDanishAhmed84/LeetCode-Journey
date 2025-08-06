class Solution(object):
    def findTheDifference(self, s , t):
        for ch in t:
            if t.count(ch) != s.count(ch):
                return ch

s="abcd"
t="abcde" 
sol=Solution()
a=sol.findTheDifference(s,t)
print(a)               
       
        