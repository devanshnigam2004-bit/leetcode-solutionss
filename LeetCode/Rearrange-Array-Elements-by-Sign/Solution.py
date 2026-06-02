1class Solution:
2    def rearrangeArray(self, nums):
3        positives = []
4        negatives = []
5
6        for num in nums:
7            if num > 0:
8                positives.append(num)
9            else:
10                negatives.append(num)
11
12        ans = []
13
14        for i in range(len(positives)):
15            ans.append(positives[i])
16            ans.append(negatives[i])
17
18        return ans