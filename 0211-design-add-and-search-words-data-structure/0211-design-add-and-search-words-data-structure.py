class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]
        
        node.isEnd = True


    def search(self, word):
        
        def dfs(j, node):
            current = node
            
            for i in range(j, len(word)):
                ch = word[i]
                
                # wildcard case
                if ch == ".":
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                # normal char case
                else:
                    if ch not in current.children:
                        return False
                    current = current.children[ch]
            
            return current.isEnd
        
        return dfs(0, self.root)