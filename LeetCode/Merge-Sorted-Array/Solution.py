1class Solution:
2    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
3        p1 = m - 1       
4        p2 = n - 1        
5        p = m + n - 1     
6
7        while p1 >= 0 and p2 >= 0:
8            if nums1[p1] > nums2[p2]:
9                nums1[p] = nums1[p1]
10                p1 -= 1
11            else:
12                nums1[p] = nums2[p2]
13                p2 -= 1
14            p -= 1
15
16        
17        while p2 >= 0:
18            nums1[p] = nums2[p2]
19            p2 -= 1
20            p -= 1