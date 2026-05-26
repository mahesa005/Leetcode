class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row and col check
        for i in range(9):
            rowSeen, colSeen = set(), set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in rowSeen:
                    return False
                if board[j][i] != '.' and board[j][i] in colSeen:
                    return False
                rowSeen.add(board[i][j])
                colSeen.add(board[j][i])

        # sub box check
        paddingi = 0
        paddingj = 0
        for k in range(3):
            paddingj = 0
            for l in range(3):
                subsetSeen = set()
                for i in range(3):
                    for j in range(3):
                        if board[i + paddingi][j + paddingj] != '.' and board[i + paddingi][j + paddingj] in subsetSeen:
                            return False
                        subsetSeen.add(board[i + paddingi][j + paddingj])
                paddingj += 3
            paddingi += 3
        return True