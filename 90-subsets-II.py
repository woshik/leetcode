class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()
        self.calculateSubsetWithDup(nums, 0, [], result)
        
        return result
    
    def calculateSubsetWithDup(self, sequence, start, container, result):
        result.append(container[:])
        
        for index in range(start, len(sequence)):
            if index != start and sequence[index] == sequence[index - 1]:
                continue
            
            container.append(sequence[index])
            self.calculateSubsetWithDup(sequence, index+1, container, result)
            container.pop()
            
s = Solution()

print(s.subsetsWithDup([1,2,2]))
