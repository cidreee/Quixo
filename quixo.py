import copy

class QuixoBot:
    def __init__(self, symbol):
        self.name = "nanabot"
        self.symbol = symbol
        self.board = [[0] * 5 for _ in range(5)]
        self.movements = {
            'U': self.up, 
            'D': self.down,
            'L': self.left,
            'R': self.right,
        }

    def up(self, board, row, col):
        for i in range(row, 0, -1):
            board[i][col] = board[i - 1][col]
        board[0][col] = self.symbol
        return True

    def down(self, board, row, col):
        for i in range(row, 4):
            board[i][col] = board[i + 1][col]
        board[4][col] = self.symbol
        return True

    def left(self, board, row, col):
        for i in range(col, 0, -1):
            board[row][i] = board[row][i - 1]
        board[row][0] = self.symbol
        return True

    def right(self, board, row, col):
        for i in range(col, 4):
            board[row][i] = board[row][i + 1]
        board[row][4] = self.symbol
        return True

    def check_win(self, board):
        for i in range(5):
            if all(board[i][j] == -1 for j in range(5)) or all(board[j][i] == -1 for j in range(5)):
                return -1
            if all(board[i][j] == 1 for j in range(5)) or all(board[j][i] == 1 for j in range(5)):
                return 1

        if all(board[i][i] == -1 for i in range(5)) or all(board[i][4-i] == -1 for i in range(5)):
            return -1
        if all(board[i][i] == 1 for i in range(5)) or all(board[i][4-i] == 1 for i in range(5)):
            return 1
        return None

    def minimax(self, board, player, depth, alpha, beta):
        winner = self.check_win(board)
        if winner is not None:
            return winner * player, None
        if depth == 2:
            return self.evaluate_board(board), None

        best_move = None
        if player == self.symbol:
            best_score = float('-inf')
        else:
            best_score = float('inf')

            # Iterar solo sobre el borde del tablero
        for row in range(5):
            for col in range(5):
                if row == 0 or row == 4 or col == 0 or col == 4:  # Solo considerar el borde del tablero
                    if board[row][col] == 0 or board[row][col] == player:
                        for move in self.movements.keys():
                            board_copy = copy.deepcopy(board)
                            if self.make_move(board_copy, row, col, move):
                                score = self.minimax(board_copy, -player, depth + 1, alpha, beta)[0]
                                if player == self.symbol:
                                    if score > best_score:
                                        best_score = score
                                        best_move = (row, col, move)
                                    alpha = max(alpha, score)
                                else:
                                    if score < best_score:
                                        best_score = score
                                        best_move = (row, col, move)
                                    beta = min(beta, score)
                                if beta <= alpha:
                                    break
        # Devolver el mejor puntaje y el mejor movimiento
        return best_score, best_move
    



    def evaluate_board(self, board):
        score = 0

        # Evaluar filas y columnas
        for i in range(5):
            row_score = sum(board[i]) * (1 + 0.1 * (i == 2 or i == 3))  # Bono por casillas centrales
            col_score = sum(board[j][i] for j in range(5)) * (1 + 0.1 * (i == 2 or i == 3))
            score += row_score + col_score

            # Evaluar líneas de símbolos separados
            row_count = sum(1 for j in range(5) if board[i][j] == self.symbol)
            col_count = sum(1 for j in range(5) if board[j][i] == self.symbol)
            score += 0.5 * row_count  # Bono por tener símbolos separados en la fila
            score += 0.5 * col_count  # Bono por tener símbolos separados en la columna

        # Evaluar diagonales
        diag1_score = sum(board[i][i] for i in range(5)) * 1.1  # Bono por diagonal central
        diag2_score = sum(board[i][4 - i] for i in range(5)) * 1.1
        score += diag1_score + diag2_score

        # Evaluar símbolos separados en diagonales
        diag1_count = sum(1 for i in range(5) if board[i][i] == self.symbol)
        diag2_count = sum(1 for i in range(5) if board[i][4 - i] == self.symbol)
        score += 0.5 * diag1_count  # Bono por tener símbolos separados en la primera diagonal
        score += 0.5 * diag2_count  # Bono por tener símbolos separados en la segunda diagonal

        # Penalizar líneas del oponente
        opponent_symbol = -1 if self.symbol == 1 else 1
        for i in range(5):
            # Penalizar por filas del oponente
            row_opponent_count = sum(1 for j in range(5) if board[i][j] == opponent_symbol)
            if row_opponent_count == 3:
                score -= 2  # Penalizar por 3 símbolos del oponente
            elif row_opponent_count == 4:
                score -= 4  # Penalizar más por 4 símbolos del oponente

            # Penalizar por columnas del oponente
            col_opponent_count = sum(1 for j in range(5) if board[j][i] == opponent_symbol)
            if col_opponent_count == 3:
                score -= 2
            elif col_opponent_count == 4:
                score -= 4

        # Penalizar por diagonales del oponente
        diag1_opponent_count = sum(1 for i in range(5) if board[i][i] == opponent_symbol)
        if diag1_opponent_count == 3:
            score -= 2
        elif diag1_opponent_count == 4:
            score -= 4

        diag2_opponent_count = sum(1 for i in range(5) if board[i][4 - i] == opponent_symbol)
        if diag2_opponent_count == 3:
            score -= 2
        elif diag2_opponent_count == 4:
            score -= 4

        return score * self.symbol


    def make_move(self, board, row, col, move):
        if move == 'U' and self.valid_move(board, 'U', row, col):
            return self.up(board, row, col)
        elif move == 'D' and self.valid_move(board, 'D', row, col):
            return self.down(board, row, col)
        elif move == 'L' and self.valid_move(board, 'L', row, col):
            return self.left(board, row, col)
        elif move == 'R' and self.valid_move(board, 'R', row, col):
            return self.right(board, row, col)
        return False

    def valid_move(self, board, direction, row, col):
        if direction == 'U' and row > 0 and (board[row ][col] == 0 or board[row][col] == self.symbol):
            return True
        if direction == 'D' and row < 4 and (board[row][col] == 0 or board[row][col] == self.symbol):
            return True
        if direction == 'L' and col > 0 and (board[row][col] == 0 or board[row][col] == self.symbol):
            return True
        if direction == 'R' and col < 4 and (board[row][col] == 0 or board[row][col] == self.symbol):
            return True
        return False



    def reset(self, symbol):
        self.symbol = symbol
        self.board = [[0] * 5 for _ in range(5)]


    def play_turn(self, board):
        self.board = board
        best_move = self.minimax(board, self.symbol, 0, float('-inf'), float('inf'))
        if best_move[1] is not None:
            row, col, move = best_move[1]
            print(best_move)
            if self.make_move(board, row, col, move):
                return board
        return board  # En caso de no encontrar un movimiento válido, devolver el tablero tal como está
