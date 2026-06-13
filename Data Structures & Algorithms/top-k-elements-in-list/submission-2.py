class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, bucket = {}, [[] for i in range(len(nums)+1)]
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for n, c in freq.items():
            bucket[c].append(n)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                if k == len(res):
                    break
                res.append(num)
        print(bucket)
        return res
