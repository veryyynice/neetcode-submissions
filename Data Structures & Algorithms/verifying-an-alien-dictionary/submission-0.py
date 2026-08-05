# class Solution:
#     #return true if the words in words list are sorted alphebitcally
#     #
#     #def lessThan(a,b,c,order_dict):
#     #    return order_dict[a]< order_dict[b] and order_dict[b]<order_dict[c]
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         #dict to map 1-26 1: h, 2: l
#         #for loop, we break out if we a<b<c, a= [0], b[0] - > a=[1], b[1]
#         #base case:a=b=c
#         #O(N)
#         #shortness???
#         order_dict = {}
#         for i in range (26):
#             order_dict[order[i]] = i
        
#         pointer = 0
#         len_array = []
#         for word in words:
#             len_array.append(len(word))
#         max_len = min(len_array)
#         for i in range(1,len(words)):
#             #i is the pointer
#             for word_index in range(1,len(words)):
#                 val = order_dict[words[word_inex-1][i]]
#                 if word[word_index-1][i]<word[word_index][i]:
#                     continue
#                 else:
#         erzwwww
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 1. Create the dictionary mapping (Corrected)
        # We map each character to its index (0-25), not (1-26).
        # Using enumerate is a clean way to do this.
        order_dict = {}
        for i, char in enumerate(order):
            order_dict[char] = i
        
        # 2. Compare adjacent words (Corrected Loop Structure)
        # We need to compare words[0] with words[1], then words[1] with words[2], etc.
        # So, we loop from 0 up to the second-to-last word.
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # 3. Compare character by character
            # We only need to check characters up to the length of the *shorter* word.
            min_len = min(len(word1), len(word2))
            
            for j in range(min_len):
                char1 = word1[j]
                char2 = word2[j]
                
                # Use the dictionary to get the "value" of each char
                val1 = order_dict[char1]
                val2 = order_dict[char2]
                
                # If they are different, we can decide
                if val1 < val2:
                    # word1 comes before word2, this pair is sorted.
                    # Break this inner loop and check the *next pair* of words.
                    break
                if val1 > val2:
                    # word1 comes after word2, the list is *not* sorted.
                    return False
                # If val1 == val2, we continue to the next character (j+1)
            
            # 4. Handle the "Prefix" Case (The "shortness???" you mentioned)
            # This 'else' block runs *only if the for j loop finished without a break*.
            # This means the words were identical up to min_len (e.g., "app" and "apple").
            else:
                if len(word1) > len(word2):
                    # This is the "apple" vs "app" case.
                    # "apple" is not sorted before "app".
                    return False

        # If we checked all pairs and never returned False, the list is sorted.
        return True
