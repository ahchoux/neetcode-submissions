from collections import defaultdict

class Solution:
    """
    def is_anagram(string: str, anagram: str) -> bool:
        if (len(string) != len(anagram)):
            return False
        
        counter1 = [0] * 26
        counter2 = [0] * 26
        
        for i in range(len(string)):
            counter1[ord(string[i])-ord('a')] += 1
            counter2[ord(anagram[i])-ord('a')] += 1
        
        return counter1 == counter2
    """
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        # sol 1: sorted
        res = defaultdict(list)

        for s in strs: # o(m) where m is num of strs
            sortedS = "".join(sorted(s)) # nlogn
            res[sortedS].append(s)

        return list(res.values())
        """

        # sol 2: 
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())



