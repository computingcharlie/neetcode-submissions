class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sets = []
        sett = []
        for i in s:
            sets.append(i)
        for i in t:
            sett.append(i)
        sett = sorted(sett)
        sets = sorted(sets)
        if sett == sets:
            return True
        else:
            return False