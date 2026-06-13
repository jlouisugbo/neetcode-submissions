class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums) # convert list into set
        for num in nums: #for num in numbers
            streak, curr = 0, num
            while curr in store: #while num is in store
                streak += 1
                curr += 1
            res = max(streak, res)
        return res
"""
stuff
"""