class Solution(object):
    def romanToInt(self, s):
        roman_mapping={
            'I':1,'V':5,'X':10,'L':50,
            'C':100,'D':500,'M':1000
        }
        total=0

        for j in range(len(s)):
            if j+1<len(s) and roman_mapping[s[j]]<roman_mapping[s[j+1]]:
                total=total-roman_mapping[s[j]]
            else:
                total=total+roman_mapping[s[j]]

        return total


sol=Solution()
print(sol.romanToInt('III'))                   

        