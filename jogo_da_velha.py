# printing the game board
# take player input
# check for win or tie
# switch players
# check for win or tie again
import time

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

gameRunning = True
currentPlayer = 'x'
winner = None


def printBoard(board):
    print(board[0], " | ", board[1], " | ", board[2])
    print("--------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("--------------")
    print(board[6], " | ", board[7], " | ", board[8])


def playerInput(board):
    inp = int(input("Escolha um número de 1 a 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Posição inválida, digite outra.")
        switchPlayer()


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = board[8]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[7] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[8] != "-":
        winner = board[2]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[8] != "-":
        winner = board[8]
        return True
    elif board[2] == board[4] == board[6] and board[6] != "-":
        winner = board[2]
        return True


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Empatou!")
        print("O jogo será fechado em 10 segundos...")
        time.sleep(5)
        gameRunning = False


def switchPlayer():
    global currentPlayer
    if currentPlayer == 'x':
        currentPlayer = 'o'
    else:
        currentPlayer = 'x'


def checkWin():
    global currentPlayer
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkVertical(board):
        currentPlayer = winner
        printBoard(board)
        print(f"Parabéns, {winner} venceu")
        print("O jogo será fechado em 10 segundos...")
        time.sleep(5)
        gameRunning = False


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    checkWin()
    checkTie(board)
