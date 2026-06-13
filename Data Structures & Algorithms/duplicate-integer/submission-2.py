class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = {}
        for i, num in enumerate(nums):
            n[num] = i
        return not (list(n.keys()) == nums)
