import moves, main

board = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]

# board = [["--", "--", "--", "--", "--", "--", "--", "--"],
#          ["--", "--", "--", "--", "--", "--", "--", "--"],
#          ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
#          ["--", "--", "--", "--", "--", "--", "--", "--"],
#          ["--", "--", "--", "--", "--", "--", "--", "--"],
#          ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
#          ["--", "--", "--", "--", "--", "--", "--", "--"],
#          ["--", "--", "--", "--", "--", "--", "--", "--"]]


moveLog = []
isWhiteTurn = True
checkMate = False

def move(playerClicks, movesPossible):

    startRow = playerClicks[0][0]
    startCol = playerClicks[0][1]
    endRow = playerClicks[1][0]
    endCol = playerClicks[1][1]

    currentMove = ((startRow, startCol), (endRow, endCol))
    moveLog.append([(startRow, startCol, board[startRow][startCol]), (endRow, endCol, board[endRow][endCol])])
    
    # print(currentMove)
    # print(movesPossible)

    if currentMove in movesPossible:

        board[endRow][endCol] = board[startRow][startCol]

        # pawn -> queen
        if board[startRow][startCol] == 'wp' and endRow == 0:
            board[endRow][endCol] = 'wq'
        elif board[startRow][startCol] == 'bp' and endRow == 7:
            board[endRow][endCol] = 'bq'
            
        board[startRow][startCol] = '--'
        return True
    
    return False


def undoMove():

    if len(moveLog) == 0:
        return

    prevMove = moveLog.pop()
    board[prevMove[0][0]][prevMove[0][1]] = prevMove[0][2]
    board[prevMove[1][0]][prevMove[1][1]] = prevMove[1][2]

    moves.changeCheck(False)


def getMoves():

    movesPossible = []
    for i in range (len(board)):
        for j in range (len(board[0])):
            piece = board[i][j]
            if (piece == '--') or (isWhiteTurn and piece[0] == 'b') or (not isWhiteTurn and piece[0] == 'w'):
                continue
            if piece[1] == 'p':
                moves.getPawnMoves(i, j, movesPossible)
            elif piece[1] == 'r':
                moves.getRookMoves(i, j, movesPossible)
            elif piece[1] == 'b':
                moves.getBishopMoves(i, j, movesPossible)
            elif piece[1] == 'n':
                moves.getKnightMoves(i, j, movesPossible)
            elif piece[1] == 'k':
                moves.getKingMoves(i, j, movesPossible)
            else:
                moves.getRookMoves(i, j, movesPossible)
                moves.getBishopMoves(i, j, movesPossible)

    return movesPossible


def validateMoves():

    movesPossible = getMoves()
    validMoves = []

    for currMove in movesPossible:

        # making move before: to check if this move can lead to check
        move(currMove, movesPossible)
        moves.changePlayer()
        opponentMoves = getMoves()
        moves.changePlayer()
        check = 0

        # checking if oppMove can take my King
        for oppMove in opponentMoves:
            if isWhiteTurn:
                if board[oppMove[1][0]][oppMove[1][1]] == 'wk':
                    check += 1
                    break
            else:
                if board[oppMove[1][0]][oppMove[1][1]] == 'bk':
                    check += 1
                    break
        # not valid move
        if check == 0:
            validMoves.append(currMove)
        undoMove()

    if(len(validMoves) == 0 and inCheck()):
        moves.changeCheck(True)

    return validMoves


def inCheck():

    moves.changePlayer()
    opponentMoves = validateMoves()
    moves.changePlayer()

    for oppMove in opponentMoves:
        if isWhiteTurn:
            if board[oppMove[1][0]][oppMove[1][1]] == 'wk':
                return True
        else:
            if board[oppMove[1][0]][oppMove[1][1]] == 'bk':
                return True
    
    return False

