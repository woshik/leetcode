class Solution:
    def isAnagram(self, s, t):
      if len(s) != len(t):
        return False
      
      return sorted(s) == sorted(t)


class Solution2:
    def isAnagram(self, s, t):
      if len(s) != len(t):
        return False
      
      hashmapS, hashmapT = {}, {}

      for n in range(len(s)):
        hashmapS[s[n]] = 1 + hashmapS.get(s[n], 0)
        hashmapT[t[n]] = 1 + hashmapT.get(t[n], 0)

      for n in hashmapS:
        if hashmapS.get(n) != hashmapT.get(n):
          return False
      
      return True
