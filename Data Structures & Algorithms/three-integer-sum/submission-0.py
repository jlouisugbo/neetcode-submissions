class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, a in enumerate(nums):
            if idx > 0 and a == nums[idx - 1]: 
                #if a == the number before it becuase its sorted
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                b, c = nums[l], nums[r]
                threeSum = a + b + c
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0: 
                    l += 1
                else:
                    res.append([a, b, c])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res