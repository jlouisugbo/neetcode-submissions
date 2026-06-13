class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        sf, tf = {}, {}
        for i in range(len(s)):
            sf[s[i]] = sf.get(s[i], 0) + 1
            tf[t[i]] = tf.get(t[i], 0) + 1

        return sf == tf