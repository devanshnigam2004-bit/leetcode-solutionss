1class Solution:
2    def isValid(self, s):
3        stack = []
4        mapping = {')': '(', '}': '{', ']': '['}
5        
6        for char in s:
7            if char in mapping:
8                top = stack.pop() if stack else '#'
9                if mapping[char] != top:
10                    return False
11            else:
12                stack.append(char)
13        
14        return not stack