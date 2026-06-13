class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        numSet = set(nums)
        res = 0
        for num in nums:
            streak = 0
            if not (num - 1) in numSet:
                while (num+1) in numSet:
                    num += 1
                    streak += 1
            res = max(res, streak) 
        return res+1
"""
stuff
"""