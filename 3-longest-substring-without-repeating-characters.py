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

s = Solution()

print(s.lengthOfLongestSubstring("pwwkew"))