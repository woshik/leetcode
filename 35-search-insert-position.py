class Solution:
    def searchInsert(self, nums, target):
      for key, value in enumerate(nums) :
        if target <= value:
          return key
      
      return len(nums)
        

s = Solution()

print(s.searchInsert([1,3,5,6], 7))