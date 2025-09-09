class Solution(object):
    def countBits(self, n):
        result=[0]
        for a in range(1,n+1):
            result.append(result[a//2] + a%2)
        return result

sol=Solution()
print(sol.countBits(0))
print(sol.countBits(1))
print(sol.countBits(2))
print(sol.countBits(3))
print(sol.countBits(4))
print(sol.countBits(5))