class Solution(object):
    def isPalindrome(self, x):
     if x<0:
        return False
     if x==0:
        return True
     if x%10==0:
        return False
     originalX=x
     num_reversed=0
     while x>0:
        last_digit=x%10
        num_reversed=num_reversed*10+last_digit
        x=x//10
     return originalX==num_reversed   
        
