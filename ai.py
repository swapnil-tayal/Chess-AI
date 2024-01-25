import engine, main, moves
import random

pieceScores = {'p':1, 'r':5, 'n':3, 'b':3, 'q':10, 'k':0}

knightScores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                 [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                 [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                 [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                 [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                 [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                 [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                 [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

bishopScores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

rookScores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

queenScores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

pawnScores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
               [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
               [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
               [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
               [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
               [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

piecePositionScores = {"wn": knightScores, "bn": knightScores[::-1],
                       "wb": bishopScores, "bb": bishopScores[::-1],
                       "wq": queenScores,  "bq": queenScores[::-1],
                       "wr": rookScores,   "br": rookScores[::-1],
                       "wp": pawnScores,   "bp": pawnScores[::-1]}

depth = 3 

def randomMove(movesPossible):
    if (len(movesPossible) == 0):
        return ()
    return random.choice(movesPossible)


def getAiMove(movesPossible):
    
    global aiMove, counter
    counter = 0
    random.shuffle(movesPossible)
    getMoveMinMax(movesPossible, engine.isWhiteTurn, depth, -1000, 1000)
    print(counter, end=" ")
    return aiMove


def getMoveMinMax(movesPossible, isWhiteTurn, cDepth, alpha, beta):

    global aiMove, counter
    counter += 1
    if cDepth == 0:
        return boardScore(engine.board)

    # white will always try to maximize its score value
    if isWhiteTurn:
        maxScore = -1000
        for currMove in movesPossible:
            engine.move(currMove, movesPossible)
            moves.changePlayer()
            nextMoves = engine.validateMoves()
            score = getMoveMinMax(nextMoves, False, cDepth-1, alpha, beta)
            
            moves.changePlayer()
            engine.undoMove()

            # trying of maximize the score
            if score > maxScore:
                maxScore = score
                if cDepth == depth:
                    aiMove = currMove
            if maxScore > alpha:
                alpha = maxScore
                
            # can say that's enough for current state, by keeping optimization in mind.
            # But can increase the diffrence(alpha - beta), and get more better 
            # move, with respect to future move.
            if alpha >= beta:
                break

        return maxScore

    # black will always try to minimize its score value
    else:
        minScore = 1000
        for currMove in movesPossible:
            engine.move(currMove, movesPossible)
            moves.changePlayer()
            nextMoves = engine.validateMoves()
            score = getMoveMinMax(nextMoves, True, cDepth-1, alpha, beta)
            
            moves.changePlayer()
            engine.undoMove()

            # trying of minimize the score
            if score < minScore:
                minScore = score
                if cDepth == depth:
                    aiMove = currMove
            if beta > minScore:
                beta = minScore
            if alpha >= beta:
                break

        return minScore
    

def boardScore(board):

    if engine.checkMate:
        if engine.isWhiteTurn:
            # white's worst case
            return -1000
        else:
            # black's worst case
            return 1000

    currentScore = 0
    for i in range (len(board)):
        for j in range (len(board[0])):
            
            piece = board[i][j]
            if piece == '--':
                continue
            
            piecePosition = 0

            if piece[1] != 'k':
                piecePosition = piecePositionScores[piece][i][j]
            if piece[0] == 'w':
                # white will add
                currentScore += pieceScores[piece[1]] + piecePosition
            elif piece[0] == 'b':
                # black will sub
                currentScore -= pieceScores[piece[1]] + piecePosition

    return currentScore
