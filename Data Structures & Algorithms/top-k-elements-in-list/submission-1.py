class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for v, c in count.items(): 
            freq[c].append(v)
        res = []
        for li in range(len(freq)-1, 0, -1):
            for num in freq[li]:
                res.append(num)
                if(len(res) == k):
                    return res
