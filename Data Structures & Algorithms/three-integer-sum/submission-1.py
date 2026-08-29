class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        st = set()
        for i in range(n-1):
            num = nums[i]
            target = -1*(num)
            l, r = i+1, n-1
            while l < r:
                add = nums[l] + nums[r]
                if add == target:
                    if i < l:
                        t = tuple([nums[i],nums[l],nums[r]])
                        st.add(t)
                    elif i > l and i < r:
                        t = tuple([nums[l],nums[i],nums[r]])
                        st.add(t)
                    else:
                        t = tuple([nums[l],nums[r],nums[i]])
                        st.add(t)
                    l += 1
                    r -= 1
                elif add > target:
                    r -= 1
                else:
                    l += 1
        arr = [list(lst) for lst in st]
        return arr
