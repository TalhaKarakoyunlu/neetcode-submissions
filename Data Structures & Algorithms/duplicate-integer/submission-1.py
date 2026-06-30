class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for num in nums:
            if num in myDict:
                return True
            else:
                myDict[num] = 0
        return False
    
if __name__ == "__main__":
    sol = Solution()
    nums_list = [0,1,2,3,4]
    print(sol.hasDuplicate(nums_list))