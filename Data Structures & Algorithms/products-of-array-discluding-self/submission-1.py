class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1]*l
        for i in range(1, l):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = [1]*l
        for i in range(l-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        output = [1]*l
        for i in range(l):
            output[i] = prefix[i]*suffix[i]
        
        return output