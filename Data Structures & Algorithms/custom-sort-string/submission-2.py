class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #order has unique chars that were sorted in custom order
        #return s premiuted so that it matches order in order
        #has 
        #order = xab, s = bbababa
        #x a b
        #b*3, a*3
        #frequencies for s
        #iterate through order, if curr in freq_s

        freq_s = {}
        for char in s:
            freq_s[char] = freq_s.get(char,0) + 1
        
        new_string = []
        #instead of set we can decrease orginal frequencies
        order_set = set(order)
        for i in range(len(order)):
            char=order[i]
            freq = freq_s.get(char,0)
            if freq>0:
                new_string.append(char*freq)

        for char in s:
            if char in order_set:
                continue
            new_string.append(char)
        return "".join(new_string)