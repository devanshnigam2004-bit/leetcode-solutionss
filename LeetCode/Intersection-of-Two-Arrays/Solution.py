1class Solution:
2    def intersection(self, nums1, nums2):
3        set1 = set(nums1)
4        set2 = set(nums2)
5
6        return list(set1 & set2)