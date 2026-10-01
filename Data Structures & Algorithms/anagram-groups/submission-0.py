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

        # sol 1: sorted
        res = defaultdict(list)

        for s in strs: # o(m) where m is num of strs
            sortedS = "".join(sorted(s)) # nlog
            res[sortedS].append(s)

        return list(res.values())

        """
        output = []

        if len(strs) <= 1:
            return [strs]
            
        print(f"print output: {output}")
        
        for string in strs: # O(n) where n is len of strs
            print("enter string in strs loop")
            print(f"len of output: {len(output)}")
            if len(output) == 0:
                output.append([string])
                print("item 0 added to output")
                continue

            for i in range(len(output)):
                
                anagram = output[i][0]

                if sorted(string) == sorted(anagram):
                    output[i].append(string)
                    break
                else:
                    continue
        
        print(f"print output: {output}")
        return output
        """