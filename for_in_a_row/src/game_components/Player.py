import numpy as np

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)

    def get_alpha_beta_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm

        This will play against either itself or a human player

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        #function to check if the board is full
        def is_terminal(board):
            for x in range(0, 7):
                if board[0][x] == 0:
                    return False
            print("true is_terminal")
            return True

        #function to check validity of given move on board
        def is_valid(board, move):
            if board[0][move] != 0:
                return False
            else:
                return True

        #function to add a valid move to the board
        def add_move(board, move, player_number):
            for x in reversed(range(0, 6)):
                if board[x][move] == 0:
                    board[x][move] = player_number
                    break


        def max_value(board, depth, alpha, beta, prev):
            if depth == 0 or is_terminal(board):
                return self.evaluation_function(board), prev

            value = float('-inf')
            for i in range(0, 7):
                temp_board = board.copy()
                if not is_valid(temp_board, i):
                    continue
                add_move(temp_board, i, self.player_number)
                value_2, move_2 = min_value(temp_board, depth - 1, alpha, beta, i)
                if value_2 > value:
                    value, move = value_2, i
                    alpha = max(alpha, value)
                if value >= beta: return value, move
            return value, move


        def min_value(board, depth, alpha, beta, prev):
            if depth == 0 or is_terminal(board):
                return self.evaluation_function(board), prev

            value = float('inf')
            for i in range(0, 7):
                temp_board = board.copy()
                if not is_valid(temp_board, i):
                    continue
                add_move(temp_board, i, self.player_number)
                value_2, move_2 = max_value(temp_board, depth - 1, alpha, beta, i)
                if value_2 < value:
                    value, move = value_2, i
                    beta = min(beta, value)
                if value <= alpha: return value, move
            return value, move


        big = float('inf')
        small = float('-inf')
        value, move = max_value(board, 4, small, big, None)
        return move


    def get_expectimax_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the expectimax algorithm.

        This will play against the random player, who chooses any valid move
        with equal probability

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        #function to check if the board is full
        def is_terminal(board):
            for x in range(0, 7):
                if board[0][x] == 0:
                    return False
            return True

        #function to check validity of given move on board
        def is_valid(board, move):
            if board[0][move] != 0:
                return False
            else:
                return True

        #function to add a valid move to the board
        def add_move(board, move, player_number):
            for x in reversed(range(0, 6)):
                if board[x][move] == 0:
                    board[x][move] = player_number
                    break

        #recursive chance option
        def random_event(board,depth):
            if depth == 0 or is_terminal(board):
                return self.evaluation_function(board)

            alpha = 0
            prob = 0

            for i in range(0, 7):
                temp_board = board.copy()
                if is_valid(temp_board, i):
                    prob += 1

            for j in range(0, 7):
                temp_board = board.copy()
                if not is_valid(temp_board, j):
                    continue
                add_move(temp_board, j, self.player_number)
                alpha = alpha + ((1 / prob) * expectimax(temp_board, depth - 1))
            return alpha


        #recursive max player option
        def expectimax(board, depth):
            if depth == 0 or is_terminal(board):
                return self.evaluation_function(board)

            alpha = float('-inf')

            for i in range(0, 7):
                temp_board = board.copy()
                if not is_valid(temp_board, i):
                    continue
                add_move(temp_board, i, self.player_number)
                alpha = max(alpha, random_event(temp_board, depth-1))
            return alpha

        #Starting max call to be able to index which move is called
        move = 0
        alpha = float('-inf')
        for i in range(0, 7):

            temp_board = board.copy()
            if not is_valid(temp_board, i):
                continue
            add_move(temp_board, i, self.player_number)

            check = alpha
            alpha = max(alpha, random_event(temp_board, 4))
            if check != alpha:
                move = i

        return move




    def evaluation_function(self, board):
        """
        Given the current state of the board, return the scalar value that
        represents the evaluation function for the current player
       
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The utility value for the current board
        """

        #arrays to hold how many combinations exist in the board
        horiz = [0, 0, 0, 0]
        vert = [0, 0, 0, 0]
        horiz_op = [0, 0, 0, 0]
        vert_op = [0, 0, 0, 0]


        curr = self.player_number
        if curr == 1:
            op = 2
        else:
            op = 1

        #horizontal checker: first if statement checks for opposition
        for x in reversed(range(0, 6)):
            for y in range(0, 4):
                in_a_row = 0
                check_op = 0
                a = board[x][y]
                b = board[x][y+1]
                c = board[x][y+2]
                d = board[x][y+3]
                template = [a, b, c, d]
                if op in template:
                    temp_op = 0
                    for i in range(0,4):
                        if template[i] == op:
                            temp_op += 1
                    if temp_op != 0:
                        horiz_op[temp_op-1] += 1
                else:
                    temp = 0
                    for i in range(0,4):
                        if template[i] == curr:
                            temp += 1
                    if temp != 0:
                        horiz[temp-1] += 1

                if op in template:
                    if curr not in template:
                        for i in range(0,4):
                            if template[i] == op:
                                check_op += 1
                                in_a_row += 1
                            elif in_a_row > 1:
                                break
                if in_a_row >= 2:
                    return -999999

                if check_op > 1:
                    return -999999


        #vertical checker: first if statement checks for opposition
        for x in reversed(range(3, 6)):
            for y in range(0, 7):
                in_a_row = 0
                check_op = 0
                a = board[x][y]
                b = board[x-1][y]
                c = board[x-2][y]
                d = board[x-3][y]
                template = [a, b, c, d]
                if op in template:
                    temp_op = 0
                    for i in range(0, 4):
                        if template[i] == op:
                            temp_op += 1
                    if temp_op != 0:
                        vert_op[temp_op - 1] += 1
                else:
                    temp = 0
                    for i in range(0, 4):
                        if template[i] == curr:
                            temp += 1
                    if temp != 0:
                        vert[temp - 1] += 1

                if op in template:
                    if curr not in template:
                        for i in range(0,4):
                            if template[i] == op:
                                check_op += 1
                                in_a_row += 1
                            elif in_a_row > 1:
                                break
                if in_a_row >= 2:
                    return -999999

                if check_op > 1:
                    return -999999


        #caculating utility for self
        utility_h = .2*horiz[0] + (.5*horiz[1]) + (2*horiz[2]) + (100*horiz[3])
        utility_v = (.5*vert[1]) + (2*vert[2]) + (100*vert[3])

        #calculating utility for opposition
        utility_hop = .5*horiz_op[0] + (2*horiz_op[1]) + (3*horiz_op[2]) + (1000 * horiz_op[3])
        utility_vop = vert_op[0] + (2 * vert_op[1]) + (3* vert_op[2]) + (1000 * vert_op[3])

        #the weight is shifted towards defending slightly more than attacking
        utility = (.6*(utility_v + utility_h)) - (utility_hop + utility_vop)

        return utility

    def get_move(self, expectimax_type = None, board = None, drawable_function = None):
        if expectimax_type == "alpha_prunning":
            return self.get_alpha_beta_move(board)
        else:
            return self.get_expectimax_move(board)


class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, expectimax_type = None, board = None, drawable_function = None):
        """
        Given the current board state select a random column from the available
        valid moves.

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)

    def get_move(self, expectimax_type = None, board = None, drawable_function = None):
        """
        Given the current board state returns the human input for next move

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        return drawable_function()

