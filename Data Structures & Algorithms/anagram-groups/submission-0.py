class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hmap= defaultdict(list)

        for s in strs:
            count=[0]*26

            for c in s:
                count[ord(c)-ord("a")]+=1
            Hmap[tuple(count)].append(s)
        return list(Hmap.values())
        