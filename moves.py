import engine, main

def changePlayer():
    engine.isWhiteTurn = not engine.isWhiteTurn

def changeCheck(flag):
    engine.checkMate = flag

def getPawnMoves(i, j, movesPossible):

    if engine.isWhiteTurn:
        if i-1 >= 0 and engine.board[i-1][j] == '--':
            movesPossible.append(((i, j), (i-1, j)))
        if i == 6 and i-1 >= 0 and engine.board[i-1][j] == '--' and i-2 >= 0 and engine.board[i-2][j] == '--':
            movesPossible.append(((i, j), (i-2, j)))
        if i-1 >= 0 and j+1 < 8 and engine.board[i-1][j+1][0] == 'b':
            movesPossible.append(((i, j), (i-1, j+1)))
        if i-1 >= 0 and j-1 >= 0 and engine.board[i-1][j-1][0] == 'b':
            movesPossible.append(((i, j), (i-1, j-1)))

    else:
        if i+1 < 8 and engine.board[i+1][j] == '--':
            movesPossible.append(((i, j), (i+1, j)))
        if i == 1 and i+1 < 8 and engine.board[i+1][j] == '--' and i+2 < 8 and engine.board[i+2][j] == '--':
            movesPossible.append(((i, j), (i+2, j)))
        if i+1 < 8 and j+1 < 8 and engine.board[i+1][j+1][0] == 'w':
            movesPossible.append(((i, j), (i+1, j+1)))
        if i+1 < 8 and j-1 >= 0 and engine.board[i+1][j-1][0] == 'w':
            movesPossible.append(((i, j), (i+1, j-1)))


def getRookMoves(i, j, movesPossible):

    for r in range(i+1, 8):
        if engine.board[r][j] == '--':
            movesPossible.append(((i, j), (r, j)))
        elif ((engine.board[r][j][0] == 'b' and engine.isWhiteTurn) or (engine.board[r][j][0] == 'w' and not engine.isWhiteTurn)):
            movesPossible.append(((i, j), (r, j)))
            break;
        else:
            break;

    for r in range(i-1,-1,-1):
        if engine.board[r][j] == '--':
            movesPossible.append(((i, j), (r, j)))
        elif (engine.board[r][j][0] == 'b' and engine.isWhiteTurn) or (engine.board[r][j][0] == 'w' and not engine.isWhiteTurn):
            movesPossible.append(((i, j), (r, j)))
            break;
        else:
            break;

    for c in range(j+1, 8):
        if engine.board[i][c] == '--':
            movesPossible.append(((i, j), (i, c)))
        elif (engine.board[i][c][0] == 'b' and engine.isWhiteTurn) or (engine.board[i][c][0] == 'w' and not engine.isWhiteTurn):
            movesPossible.append(((i, j), (i, c)))
            break;
        else:
            break;

    for c in range(j-1,-1,-1):
        if engine.board[i][c] == '--':
            movesPossible.append(((i, j), (i, c)))
        elif (engine.board[i][c][0] == 'b' and engine.isWhiteTurn) or (engine.board[i][c][0] == 'w' and not engine.isWhiteTurn):
            movesPossible.append(((i, j), (i, c)))
            break;
        else:
            break;


def getBishopMoves(i, j, movesPossible):

    r = i-1
    c = j-1
    while r >= 0 and c >= 0:
        if engine.board[r][c] == '--':
            movesPossible.append(((i, j), (r, c)))
        elif (engine.board[r][c][0] == 'b' and engine.isWhiteTurn) or (engine.board[r][c][0] == 'w' and not engine.isWhiteTurn):
            movesPossible.append(((i, j), (r, c)))
            break
        else:
            break
        r -= 1
        c -= 1

    r = i+1
    c = j+1
    while r < 8 and c < 8:
        if engine.board[r][c] == '--':
            movesPossible.append(((i, j), (r, c)))
        elif (engine.board[r][c][0] == 'b' and engine.isWhiteTurn) or (engine.board[r][c][0] == 'w' and not engine.isWhiteTurn):
            movesPossible.append(((i, j), (r, c)))
            break
        else:
            break
        r += 1
        c += 1

    r = i+1
    c = j-1
    while r < 8 and c >= 0:
        if engine.board[r][c] == '--':
            movesPossible.append(((i, j), (r, c)))
        elif (engine.board[r][c][0] == 'b' and engine.isWhiteTurn) or (engine.board[r][c][0] == 'w' and not engine.isWhiteTurn):
            movesPossible.append(((i, j), (r, c)))
            break
        else:
            break
        r += 1
        c -= 1

    r = i-1
    c = j+1
    while r >= 0 and c < 8:
        if engine.board[r][c] == '--':
            movesPossible.append(((i, j), (r, c)))
        elif (engine.board[r][c][0] == 'b' and engine.isWhiteTurn) or (engine.board[r][c][0] == 'w' and not engine.isWhiteTurn):
            movesPossible.append(((i, j), (r, c)))
            break
        else:
            break
        r -= 1
        c += 1


def getKnightMoves(i, j, movesPossible):

    dx = [-2,-1,1,2,-2,-1,1,2];
    dy = [-1,-2,-2,-1,1,2,2,1];

    for k in range(8):
        r = i + dx[k]
        c = j + dy[k]
        if r >= 0 and r < 8 and c < 8 and c >= 0:
            if engine.board[r][c] == '--':
                movesPossible.append(((i, j), (r, c)))
            elif (engine.board[r][c][0] == 'b' and engine.isWhiteTurn) or (engine.board[r][c][0] == 'w' and not engine.isWhiteTurn):
                movesPossible.append(((i, j), (r, c)))


def getKingMoves(i, j, movesPossible):

    dx = [1,-1,1,-1,1,0,-1,0];
    dy = [1,-1,-1,1,0,1,0,-1];

    for k in range(8):
        r = i + dx[k]
        c = j + dy[k]
        if r >= 0 and r < 8 and c < 8 and c >= 0:
            if engine.board[r][c] == '--':
                movesPossible.append(((i, j), (r, c)))
            elif (engine.board[r][c][0] == 'b' and engine.isWhiteTurn) or (engine.board[r][c][0] == 'w' and not engine.isWhiteTurn):
                movesPossible.append(((i, j), (r, c)))

