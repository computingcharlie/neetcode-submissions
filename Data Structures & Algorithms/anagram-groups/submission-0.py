class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap most efficient and least mem
        map = defaultdict(list)
        for i in strs:
            count = [0] * 26 #constraints are lowercase a-z, hence 26 chars

            for c in i:
                count[ord(c) - ord("a")] += 1
            
            map[tuple(count)].append(i)
        return list(map.values())