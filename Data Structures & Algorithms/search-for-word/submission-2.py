class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        result = []
        
        def dfs(r,c,word, index, visited):
            found = False
            if index == len(word):
                return True
            if r<0 or r>=row or c<0 or c>=col:
                return False
            if (r,c) in visited:
                return False
            
            if board[r][c] != word[index]:
                return False

            visited.add((r,c))

            found = (dfs(r+1,c, word, index+1, visited) or
                    dfs(r-1,c, word, index+1, visited) or 
                    dfs(r,c+1, word, index+1, visited) or 
                    dfs(r,c-1, word, index+1, visited))
            visited.remove((r,c))

            return found
        found = False
        for r in range(row):
            for c in range(col):
                if dfs(r,c, word, 0, set()):
                    found = True
                    break
            if found:
                break
            
        
        return found 