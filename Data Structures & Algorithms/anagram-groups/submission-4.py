class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(len(strs)):
            store = [0] * 26
            for c in strs[i]:
                store[ord(c)-ord('a')] += 1
            res[tuple(store)].append(strs[i])
        return list(res.values())