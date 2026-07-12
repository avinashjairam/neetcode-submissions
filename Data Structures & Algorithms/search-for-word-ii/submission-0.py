class TrieNode:
    def __init__(self):
        # dictionary to store child nodes with characters as keys 
        self.children = {}
        # flag to mark the end of a valid word
        self.isWord = False

    def addWord(self, word):
        # start from the current node
        cur = self

        for c in word:
            if c not in cur.children: # if the character doesn't exist in children, create a new one
                cur.children[c] = TrieNode()
            cur = cur.children[c] # move to the child node

        cur.isWord = True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create the root of our Trie
        root = TrieNode()

        # Add all the words to the Trie
        for w in words:
            root.addWord(w)

        # Get dimensions of the board
        ROWS, COLS = len(board), len(board[0])

        # Use a set to store results (to avoid duplicates)
        # and a set to track visited cells in current path
        res, visit = set(), set()

        def dfs(r, c, node, word):
            # bases cases -> return if out of bounds, cell already visted in current path
            # or current letter isn't in Trie's children 
            if (r < 0 or c < 0) or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            # mark current cell as visited 
            visit.add((r,c))
            # move to the next node in the trie based on current char
            node = node.children[board[r][c]]
            # add current character to our current word
            word += board[r][c]
            # if we've reached a valid word in our Trie, add to results
            if node.isWord:
                res.add(word)

            # recursively explore all 4 directions
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            # backtrack to remove current cell from visited set
            visit.remove((r,c))
        
        # start dfs from every cell in the board 
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root,'')

        return list(res)
            












