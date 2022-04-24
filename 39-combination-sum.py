class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.calculateCombinationSum(candidates, 0, [], target, result)
        return result

    def calculateCombinationSum(self, sequence, index, container, target, result):
        if index == len(sequence) or target == 0:
            if target == 0:
                result.append(container[:])
            return

        if sequence[index] <= target:
            container.append(sequence[index])
            self.calculateCombinationSum(sequence, index, container, target - sequence[index], result)
            container.remove(sequence[index])

        self.calculateCombinationSum(sequence, index+1, container, target, result)


s = Solution()

print(s.combinationSum([2, 3,5], 8))
