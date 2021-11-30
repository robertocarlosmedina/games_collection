import pygame

class Tic_Tac_Toe:
    def __init__(self, screen) -> None:
        self.branco = " "
        self.token = ["X", "O"]
        self.make_board()

    def make_board(self):
        self.board = [
            [self.branco, self.branco, self.branco],
            [self.branco, self.branco, self.branco],
            [self.branco, self.branco, self.branco],
        ]
    
    def get_board(self) -> list:
        return self.board

    def getInputValido(self, board = None, jogador = None, verificaGanhador = None, start_pos = None) -> int:
        start_pos = [int(value) for value in start_pos]
        x = start_pos[0] + 9
        y = start_pos[1] + 9
        mouse_pos = pygame.mouse.get_pos()
        for i in range(3):
            for j in range(3):
                click = pygame.mouse.get_pressed(3)
                if click[0] and mouse_pos[0] in range(x, x + start_pos[2]) and mouse_pos[1] in range(y, y + start_pos[2]):
                    return i, j
                x += 2 + start_pos[2]
            x = start_pos[0] + 9
            y += start_pos[2] + 2
        return None, None

    def verificaMovimento(self, i , j):
        if(self.board[i][j] == self.branco):
            return True
        else:
            return False

    def fazMovimento(self, i, j, jogador):
        self.board[i][j] = self.token[jogador]

    def verificaGanhador(self):
        # linhas 
        for i in range(3):
            if(self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] != self.branco):
                return self.board[i][0]

        # coluna
        for i in range(3):
            if(self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] != self.branco):
                return self.board[0][i]

        # diagonal principal
        if(self.board[0][0] != self.branco and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]):
            return self.board[0][0]

        # diagonal secundaria
        if(self.board[0][2] != self.branco and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]):
            return self.board[0][2]

        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == self.branco):
                    return False

        return "EMPATE"
