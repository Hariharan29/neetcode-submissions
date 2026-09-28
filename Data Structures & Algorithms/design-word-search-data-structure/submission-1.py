class node:
    def __init__(self):
        self.children = {}
        self.endof = False
class WordDictionary:

    def __init__(self):
        self.root = node()
        
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=node()
            cur=cur.children[c]
        self.endof= True
        

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                else:
                    if c not in cur.children:
                        return False
                    cur=cur.children[c]
                return cur.endof
        return dfs(0,self.root)

                
