class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
if __name__ == "__main__":
    sol = Solution()
    nums_list = [0,1,2,3,4]
    print(sol.hasDuplicate(nums_list))