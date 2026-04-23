1class Solution:
2    def reverseString(self, s):
3        left, right = 0, len(s) - 1
4        
5        while left < right:
6            s[left], s[right] = s[right], s[left]
7            left += 1
8            right -= 1