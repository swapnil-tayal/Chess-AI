import pygame as p
import engine, ai
import time

height = 512
width = 512
blocks = 8
blockSize = 64
pieces = {}

def loadPieces():
    images = ['wp', 'wb', 'wr', 'wk', 'wq', 'wn', 'bp', 'bb', 'br', 'bk', 'bq', 'bn']
    for i in images:
        pieces[i] = p.transform.scale(p.image.load("images/" + i + ".png"), (blockSize, blockSize))


def main():

    global canAiLoad, aiBlack, aiWhite
    p.init()
    screen = p.display.set_mode((width, height))
    screen.fill(p.Color('white'))
    loading = True
    loadPieces()
    blockSelected = ()
    playerClicks = []
    movesPossible = engine.validateMoves()
    aiBlack = True
    aiWhite = False
    canAiLoad = False

    while loading:

        # print(engine.isWhiteTurn)
        for e in p.event.get():

            if e.type == p.MOUSEBUTTONDOWN:
                
                # getting current position
                coordinates = p.mouse.get_pos()
                col = coordinates[0] // blockSize
                row = coordinates[1] // blockSize

                # select box onClick
                blockSelected = (row, col)
                playerClicks.append(blockSelected)

                # twice click then move
                if(len(playerClicks) == 2):
                    
                    # print(playerClicks)
                    isMoveMade = engine.move(playerClicks, movesPossible)
                    playerClicks = []
                    blockSelected = ()
                    if isMoveMade:
                        engine.isWhiteTurn = not engine.isWhiteTurn
                        movesPossible = engine.validateMoves()


            # z for undo move
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    engine.undoMove()
                    engine.isWhiteTurn = not engine.isWhiteTurn


            if e.type == p.QUIT:
                loading = False

        
        if canAiLoad and ((not engine.isWhiteTurn and aiBlack) or (engine.isWhiteTurn and aiWhite)):

            aiStartTime = int(round(time.time() * 1000))
            print("AI thinks....", end="")
            
            aiMove = ai.getAiMove(movesPossible)
            aiEndTime = int(round(time.time() * 1000))
            print((aiEndTime-aiStartTime)/1000, end="s\n")

            if len(aiMove) != 0:
                engine.move(aiMove, movesPossible)
                engine.isWhiteTurn = not engine.isWhiteTurn
            movesPossible = engine.validateMoves()
            canAiLoad = False


        setUpBoard(screen, blockSelected, movesPossible)  
        p.display.flip()


def setUpBoard(screen, blockSelected, movesPossible):
    
    global canAiLoad, aiBlack, aiWhite
    # checked board
    for i in range (blocks):
        for j in range (blocks):
            color = ()
            if((i+j)%2 == 0):
                color = (118, 148, 87)
            else:
                color = (238, 238, 211)
            p.draw.rect(screen, color , p.Rect(j * blockSize, i * blockSize, blockSize, blockSize))

    if (engine.isWhiteTurn and aiWhite) or (not engine.isWhiteTurn and aiBlack):
        canAiLoad = True

    # highlightSquares
    showMoves(screen, blockSelected, movesPossible)

    # setup pieces
    for i in range (blocks):
        for j in range (blocks):
            piece = engine.board[i][j]
            if piece != '--':
                screen.blit(pieces[piece], p.Rect(j * blockSize, i * blockSize, blockSize, blockSize))


def showMoves(screen, blockSelected, movesPossible):

    if len(blockSelected) == 0:
        return
    r = blockSelected[0]
    c = blockSelected[1]
    s = p.Surface((blockSize, blockSize))
    s.set_alpha(100)
    s.fill(p.Color("blue")) 
    screen.blit(s, (c * blockSize, r * blockSize))
    s.fill(p.Color("yellow"))

    for move in movesPossible:
        if move[0][0] == r and move[0][1] == c:
            screen.blit(s, (move[1][1] * blockSize, move[1][0] * blockSize))


if __name__ == "__main__":
    main()

