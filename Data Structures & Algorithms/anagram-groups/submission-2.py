class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 1:
            return [strs]
        
# A standard dictionary throws a KeyError if you try to modify a key that does not exist yet. A defaultdict(list) automatically creates an empty list [] for any missing key the moment you access or append to it.

        mp = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            mp[tuple(cnt)].append(s)
        
        return list(mp.values())
        

