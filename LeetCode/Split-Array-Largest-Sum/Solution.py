1class Solution:
2    def splitArray(self, nums: list[int], k: int) -> int:
3
4        def canSplit(mid):
5            count = 1
6            current = 0
7            for num in nums:
8                if current + num > mid:
9                    count += 1
10                    current = 0
11                current += num
12            return count <= k
13
14        low = max(nums)       
15        high = sum(nums)     
16
17        while low < high:
18            mid = (low + high) // 2
19            if canSplit(mid):
20                high = mid
21            else:
22                low = mid + 1
23
24        return low