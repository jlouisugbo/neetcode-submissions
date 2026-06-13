class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  #initialize a dictionary of 
        #where the default value for any nonexistent key is a list

        for s in strs: #for string in teh strings
            count = [0] * 26 # 26 0s 

            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)
        return list(res.values())

                