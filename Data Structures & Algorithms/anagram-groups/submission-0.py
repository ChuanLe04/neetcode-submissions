class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempdict = {}

        for i in strs:
            sorted_key = "".join(sorted(i))

            if sorted_key not in tempdict:
                tempdict[sorted_key] = []
            
            tempdict[sorted_key].append(i)

        return list(tempdict.values())
            
