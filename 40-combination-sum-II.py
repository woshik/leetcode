class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.calculateCombinationSum(candidates, 0, target, [], result)
        return result
    
    def calculateCombinationSum(self, sequence, start, target, container, result):
        if start >= len(sequence) or target == 0:
            if target == 0:
                result.append(container[:])
            return

        
        for index in range(start, len(sequence)):
            if index != start and sequence[index] == sequence[index - 1]:
                continue
            
            if sequence[index] > target:
                break
            
            if sequence[index] <= target:
                container.append(sequence[index])
                self.calculateCombinationSum(sequence, index+1, target - sequence[index], container, result)
                container.pop()

s = Solution()

print(s.combinationSum2([10,1,2,7,6,1,5], 8))