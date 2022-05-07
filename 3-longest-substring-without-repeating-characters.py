class Solution:
    def lengthOfLongestSubstring(self, s):
        largestStringCount = 0
        tempList = []

        for char in s:
          if char in tempList:
            tempList = tempList[tempList.index(char)+1:]

          tempList.append(char)  
          largestStringCount = max(len(tempList), largestStringCount)
          
          
        return largestStringCount

class Solution2:
    def lengthOfLongestSubstring(self, s):
        leftPointer, largestStringCount = 0, 0
        hashMap = {}

        for rightPointer in range(len(s)):
          if hashMap.get(s[rightPointer]) != None:
            leftPointer = max(hashMap[s[rightPointer]] + 1, leftPointer)
          
          largestStringCount = max(largestStringCount, rightPointer-leftPointer+1)
          hashMap[s[rightPointer]] = rightPointer
                    
        return largestStringCount

s = Solution2()

print(s.lengthOfLongestSubstring("abcabcbb"))