1import random
2
3class Solution:
4    def findKthLargest(self, nums, k):
5        target = len(nums) - k
6        left = 0
7        right = len(nums) - 1
8
9        while left <= right:
10            pivot = nums[random.randint(left, right)]
11
12            lt = left
13            i = left
14            gt = right
15
16            while i <= gt:
17                if nums[i] < pivot:
18                    nums[lt], nums[i] = nums[i], nums[lt]
19                    lt += 1
20                    i += 1
21                elif nums[i] > pivot:
22                    nums[i], nums[gt] = nums[gt], nums[i]
23                    gt -= 1
24                else:
25                    i += 1
26
27            if target < lt:
28                right = lt - 1
29            elif target > gt:
30                left = gt + 1
31            else:
32                return nums[target]