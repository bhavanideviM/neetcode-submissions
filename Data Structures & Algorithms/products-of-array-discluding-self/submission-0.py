class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0]*n
        
        for i in range(0, n):
            prod =1
            
            for j in range(0, n):
                if j!=i:
                    prod*=nums[j]
            res[i]=prod
        return res