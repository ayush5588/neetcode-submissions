class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 0 or n == 1:
            return [strs]
        
        mp = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c)-ord('a')] += 1
            mp[tuple(arr)].append(s)
        
        return list(mp.values())
