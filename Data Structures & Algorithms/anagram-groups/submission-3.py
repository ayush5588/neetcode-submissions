class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            mp[tuple(arr)].append(s)
        
        return list(mp.values())