# Last updated: 10/2/2025, 6:01:27 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum = 0
        for ch in nums:
            sum+=ch
            res.append(sum)
        return res