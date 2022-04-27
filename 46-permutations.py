class Solution:
    def permute(self, nums):
        result = []
        self.calculatePermutation(nums, {}, [], result)
        return result
        
    def calculatePermutation(self, sequence, map, container, result):
        if len(sequence) == len(container):
            result.append(container[:])
            return
        
        for index in range(0, len(sequence)):
            if map.get(index):
                continue
            
            container.append(sequence[index])
            map[index] = True
            self.calculatePermutation(sequence, map, container, result)
            map[index] = False
            container.pop()
            
s = Solution()

print(s.permute([1,2,3]))