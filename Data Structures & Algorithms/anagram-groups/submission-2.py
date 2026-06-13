class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            bucket = [0] * 26
            for c in s:
                bucket[ord(c)-ord('a')] += 1
            res[tuple(bucket)].append(s)
        return list(res.values())

"""
- we have groups of anagrams
- what we want to do is group them by basically a psuedo "bucket sort" 
based on their ascii value
- defaultdict of lists
- the dictionary key will be a tuple holding said bucket sorted list because
lists are mutable and keys have to be immutable/hashable so tuple it
- then once you find a match in the dictionary, append the word to the list
- return the list of values so do list(res.values())
"""