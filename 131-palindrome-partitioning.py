class Solution:
    def partition(self, s):
      result = []
      self.calculatePartition(s, [], result)
      return result

    def calculatePartition(self, sequence, container, result):
      if len(sequence) == 0:
        result.append(container[:])

      
      for index in range(1, len(sequence)+1):
        tempInput = sequence[:index]
        if tempInput == tempInput[::-1]:
          container.append(tempInput)
          self.calculatePartition(sequence[index:], container, result)
          container.pop()
        
s = Solution()

print(s.partition("aab"))