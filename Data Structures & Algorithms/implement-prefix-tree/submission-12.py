class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:
    #97
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for index in range(len(word)):
            char = word[index]
            i = ord(char) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
                curr = curr.children[i]
            else: curr = curr.children[i]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] ==None:return False
            curr = curr.children[i]
        #print ("finished for loop")
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if curr.children[i] ==None:return False
            curr = curr.children[i]
        return True
        