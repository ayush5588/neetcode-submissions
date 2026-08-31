class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)

        mps = defaultdict(int)
        mpt = defaultdict(int)

        for i in range(n):
            mps[s[i]] += 1
            mpt[t[i]] += 1
        
        return mps == mpt