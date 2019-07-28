# Checks if the game has been Won or Not
def gameOver(state):
    # rows
    for i in range(3):
        if state[i][0] == state[i][1] and state[i][1] == state[i][2]:
            if state[i][0] != '-':
                return True
    # cols
    for i in range(3):
        if state[0][i] == state[1][i] and state[1][i] == state[2][i]:
            if state[0][i] != '-':
                return True
    # diags
    if state[0][0] == state[1][1] and state[1][1] == state[2][2]:
        if state[0][0] != '-':
            return True

    if state[0][2] == state[1][1] and state[1][1] == state[2][0]:
        if state[0][2] != '-':
            return True

    return False


# Checks if there is unmarked cell left on Board

def emptyCellLeft(state):
    for i in state:
        if '-' in i:
            return True
    return False

# Returns a list of unmarked cells on the board


def get_empty_cells(state):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '-':
                empty_cells.append([i, j])
    return empty_cells

# Returns the Opponent


def get_opponent(player):
    return 'O' if player == 'X' else 'X'

# Converts the Move Number in its respective row and column values


def getIndices(number):
    return [(number-1)//3, (number-1) % 3]

# Makes the move on the Board


def makeMove(state, player, player_move):
    state[player_move[0]][player_move[1]] = player
    return

# Prints the state of the board


def printBoard(state):
    print(' ' + state[0][0] + ' | ' + state[0][1] + ' | ' + state[0][2])
    print('-----------')
    print(' ' + state[1][0] + ' | ' + state[1][1] + ' | ' + state[1][2])
    print('-----------')
    print(' ' + state[2][0] + ' | ' + state[2][1] + ' | ' + state[2][2])
    return

# Checks if Game has been won by any player or not. If won, Returns the Player Symbol, '-' otherwise


def get_status(state):
    # rows
    for i in range(3):
        if state[i][0] == state[i][1] and state[i][1] == state[i][2]:
            if state[i][0] == 'X':
                return 'X'
            elif state[i][0] == 'O':
                return 'O'
    # cols
    for i in range(3):
        if state[0][i] == state[1][i] and state[1][i] == state[2][i]:
            if state[0][i] == 'X':
                return 'X'
            elif state[0][i] == 'O':
                return 'O'
    # diags
    if state[0][0] == state[1][1] and state[1][1] == state[2][2]:
        if state[0][0] == 'X':
            return 'X'
        elif state[0][0] == 'O':
            return 'O'
    if state[0][2] == state[1][1] and state[1][1] == state[2][0]:
        if state[0][0] == 'X':
            return 'X'
        elif state[0][0] == 'O':
            return 'O'

    return '-'

# Prints the result after the Game is Over


def printResult(state, player):
    symbol = get_status(state)
    if symbol == player:
        print("Player Beat the AI !!!")
    elif symbol == get_opponent(player):
        print("AI Beat the Player.")
    else:
        print('Its a Draw.')

# Finds the Best move for the given Board


def getBestMove(state, player):

    bestMove = [-1, -1]
    bestScore = -10

    for cell in get_empty_cells(state):
        state[cell[0]][cell[1]] = player
        score = miniMax(state, player, get_opponent(player), 0)
        state[cell[0]][cell[1]] = '-'
        if score > bestScore:
            bestScore = score
            bestMove = cell
    return bestMove

# Minimax Algorithm
# state - current state of the board for which the best value is to be calculated
# computer - symbol of the AI
# player - symbol for which minimax algorithm is called
# depth - depth of the search


def miniMax(state, computer, player, depth):
    if gameOver(state):
        if computer != player:
            return 10 - depth
        else:
            return -10 + depth

    if not emptyCellLeft(state):
        return 0

    if player == computer:
        bestScore = -10
        for cell in get_empty_cells(state):
            state[cell[0]][cell[1]] = player
            score = miniMax(state, computer, get_opponent(player), depth + 1)
            state[cell[0]][cell[1]] = '-'
            bestScore = max(bestScore, score)
        return bestScore

    else:
        bestScore = 10
        for cell in get_empty_cells(state):
            state[cell[0]][cell[1]] = player
            score = miniMax(state, computer, get_opponent(player), depth + 1)
            state[cell[0]][cell[1]] = '-'
            bestScore = min(bestScore, score)
        return bestScore


# Driver Program
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
VALID_SYMBOLS = ['x', 'X', 'o', 'O']
player = input("Choose Symbol. 'X' or 'O' : ")
print("Move Numbers follow the below Pattern:\n 1 | 2 | 3\n--------\n 4 | 5 | 6\n--------\n 7 | 8 | 9")
moves_count = 0
if player not in VALID_SYMBOLS:
    exit

if player == 'x' or player == 'X':
    player = 'X'
    opponent = 'O'
else:
    player = 'O'
    opponent = 'X'

if player == 'X':
    while((not gameOver(board)) and emptyCellLeft(board)):
        player_move = getIndices(
            int(input("\nChoose your next move ( 1 to 9 ): ")))
        makeMove(board, player, player_move)
        moves_count += 1
        printBoard(board)

        if moves_count == 9:
            break
        opponent_move = getBestMove(board, opponent)
        makeMove(board, opponent, opponent_move)
        moves_count += 1
        print("\nComputer's Move: ", (opponent_move[0]*3 + opponent_move[1])+1)
        printBoard(board)

else:
    while((not gameOver(board)) and emptyCellLeft(board)):
        opponent_move = getBestMove(board, opponent)
        makeMove(board, opponent, opponent_move)
        moves_count += 1
        print("\nComputer's Move: ", (opponent_move[0]*3 + opponent_move[1])+1)
        printBoard(board)

        if moves_count == 9:
            break
        player_move = getIndices(
            int(input("\nChoose your next move ( 1 to 9 ): ")))
        makeMove(board, player, player_move)
        moves_count += 1
        printBoard(board)

printResult(board, player)
