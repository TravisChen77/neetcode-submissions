class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in grams:
                words = []
                grams[key] = words
                words.append(word)
            else:
                grams[key].append(word)
        output = list(grams.values())
        return output
                

        
            
