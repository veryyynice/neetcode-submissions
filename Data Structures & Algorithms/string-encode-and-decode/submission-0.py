class Solution:
    #. # for delim
    #skip    first # ____n_____ # , then you encounter ?____n___?
    def encode(self, strs: List[str]) -> str:
        new_string = ""
        #how many words
        # new_string+=("#"+str(len(strs))+"#")
        for i in strs:
            new_string+= ("?"+str(len(i))+"?")
            new_string+= i
        return new_string

    def decode(self, s: str) -> List[str]:
        res = []
        # list_len = 0
        # start_index = 0
        # for char_index in range(len(s)):
        #     if s[char_index] == "#":
        #         list_len = s[:char_index]
        #         start_index = char_index
        # s = s[char_index:]

        #python splicing ending index not included
        curr_index = 1
        word_length = 0
        while len(s) >= 1 or len(s) !=0 :
            print(len(s))
            while s[curr_index] != "?":
                curr_index += 1
            word_length = int(s[1:curr_index])
            word = s[(curr_index+1):(curr_index+1+word_length)]
            
            res.append(word)

            s= s[(curr_index+1+word_length):]
            curr_index =1
        return (res)
