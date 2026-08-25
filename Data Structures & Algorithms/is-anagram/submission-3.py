class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicts = dict()
        dictt = dict()
        for letter in s:
            if letter in dicts:
                dicts[letter]+=1
            else:
                dicts[letter] = 1
        for letter in t:
            if letter in dictt:
                dictt[letter] += 1
            else:
                dictt[letter] = 1
    
        if dicts == dictt:
            return True
        else:
            return False