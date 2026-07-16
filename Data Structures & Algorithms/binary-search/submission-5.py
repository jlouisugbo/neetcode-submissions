class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if target > nums[l]:
                l += 1
            if target < nums[r]:
                r -= 1
            print("L is ", l)
            print("R is ", r)
            
        return -1