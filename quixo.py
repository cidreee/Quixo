class Quixo:
    def __init__(self):
        self.board = [['.'] * 5 for _ in range(5)]

        # Diccionario 

    #-------------- movimientos ---------------------------------
    def up(self, row, col, piece):
        if row == 4:
            return False
        for i in range(row, 0, -1):
            self.board[i][col] = self.board[i - 1][col]
        self.board[4][col] = piece

    def down(self, row, col, piece):
        if row == 0:
            return False
        for i in range(row, 4):
            self.board[i][col] = self.board[i + 1][col]
        self.board[0][col] = piece

    def left(self, row, col, piece):
        if col == 4:
            return False
        for i in range(col, 0, -1):
            self.board[row][i] = self.board[row][i - 1]
        self.board[row][4] = piece

    def right(self, row, col, piece):
        if col == 0:
            return False
        for i in range(col, 4):
            self.board[row][i] = self.board[row][i + 1]
        self.board[row][0] = piece
    # ------------------------------------------------------------
    
    def check_win(self):
        # Revisamos las verticales u horizontales
        for i in range(5):
            if all(self.board[i][j] == 'X' for j in range(5)) or all(self.board[j][i] == 'X' for j in range(5)):
                return 'X'
            if all(self.board[i][j] == 'O' for j in range(5)) or all(self.board[j][i] == 'O' for j in range(5)):
                return 'O'
            
        # Revisamos las diagonales
        if all(self.board[i][i] == 'X' for i in range(5)) or all(self.board[i][4-i] == 'X' for i in range(5)):
            return 'X'
        if all(self.board[i][i] == 'O' for i in range(5)) or all(self.board[i][4-i] == 'O' for i in range(5)):
            return 'O'
        return None

    def play(self):
        pass
     
    def print_board(self):
        for i in self.board:
            print(i)

game = Quixo()

game.print_board()
print(" ")

result = game.check_win()
print(result)
