class Solution:
    def subsets(self, nums):
        result = []
        self.calculateSubsets(nums, 0, [], result)
        return result
        
    def calculateSubsets(self, sequence, start, container, result):
        if start >= len(sequence):
            result.append(container[:])
            return
        
        container.append(sequence[start])
        
        self.calculateSubsets(sequence, start+1, container, result)
        
        container.remove(sequence[start])
        
        self.calculateSubsets(sequence, start+1, container, result)
        

s = Solution()

print(s.subsets([1,2,3]))