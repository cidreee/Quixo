import random

class Quixo:
    def __init__(self):
        self.board = [['.'] * 5 for _ in range(5)]

        self.player = 'X'
        self.opponent = 'O'

        # Diccionario 

    #-------------- movimientos ---------------------------------
    def up(self, row, col, piece):
        if row == 4:
            return False
        for i in range(row, 4):
            self.board[i][col] = self.board[i + 1][col]
        self.board[4][col] = piece

    def down(self, row, col, piece):
        if row == 0:
            return False
        for i in range(row, -1, -1):
            print(i)
            self.board[i][col] = self.board[i - 1][col]
        self.board[0][col] = piece

    def left(self, row, col, piece):
        if col == 4:
            return False
        for i in range(col, 4):
            self.board[row][i] = self.board[row][i + 1]
        self.board[row][4] = piece

    def right(self, row, col, piece):
        if col == 0:
            return False
        for i in range(col, -1, -1):
            print(i)
            self.board[row][i] = self.board[row][i - 1]
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
    
    def choose_mode(self):
        while True:
            mode = input("Elige un modo de juego: (1) Player vs Player (2) Player vs Computer: ")
            if mode in ['1', '2']:
                self.mode = 'PvP' if mode == '1' else 'PvE'
                break
            else:
                print("Opción inválida.")
    
    def choose_piece(self):
        while True:
            piece = input("Elige tu pieza: (X o O): ").upper()
            if piece in ['X', 'O']:
                self.player = piece
                self.opponent = 'O' if piece == 'X' else 'X'
                break
            else:
                print("Opción inválida.")

    def play(self):
        self.choose_mode()
        self.choose_piece()
        while not self.check_win():
            self.print_board()
            if self.player == 'X' or self.mode == 'PvP':
                row, col, move = self.get_player_move()
                self.make_move(row, col, move, self.player)
            else:
                self.bot_move()
            if self.check_win():
                self.print_board()
                print(f"Player {self.check_win()} wins!")
                break
            self.switch_player()

    def switch_player(self):
        self.player, self.opponent = self.opponent, self.player
    
    def is_valid_move(self, row, col, piece):
        current_pice, flipped = self.board[row][col]
        return flipped == '.' or current_pice == piece


    def make_move(self, row, col, move, piece):
        if move == 'up':
            self.up(row, col, piece)
        elif move == 'down':
            self.down(row, col, piece)
        elif move == 'left':
            self.left(row, col, piece)
        elif move == 'right':
            self.right(row, col, piece)


    def bot_move(self):
        row, col, move = random.choice([(i, j, m) for i in range(5) for j in range(5) for m in ['up', 'down', 'left', 'right']])
        self.make_move(row, col, move, self.opponent)

    
    def get_player_move(self):
        while True:
            try:
                row = int(input("Ingresa la fila (0-4): "))
                col = int(input("Ingresa la columna (0-4): "))

                if row in range(5) and col in range(5):
                    if self.is_edge(row, col) and self.is_valid_move(row, col, self.player):
                        break
                    else:
                        print("Solo puedes tomar piezas de las orillas que no hayan sido volteadas o sean de tu pieza.")
                else:
                    print("Posición inválida. Debe estar entre 0 y 4.")
                    
            except ValueError:
                print("Error. Ingresa números para la fila y la columna.")

        while True:
            move = input("Ingresa el movimiento (up, down, left, right): ").lower()
            if move in ['up', 'down', 'left', 'right']:
                return row, col, move
            else:
                print("Movimiento inválido. Debe ser 'up', 'down', 'left' o 'right'.")

    
    def is_edge(self, row, col):
        return row == 0 or row == 4 or col == 0 or col == 4

     
    def print_board(self):
        for i in self.board:
            print(i)

game = Quixo()

game.print_board()
game.right(0, 2, 'X')

print('/n')
game.print_board()
