class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = [[] for i in range(n+1)]

        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        
        for num, freq in mp.items():
            arr[freq].append(num)
        
        ans = []
        for i in range(len(arr)-1,-1,-1):
            for j in range(len(arr[i])-1,-1,-1):
                if k > 0:
                    ans.append(arr[i][j])
                    k -= 1
                else:
                    return ans
        
        return ans