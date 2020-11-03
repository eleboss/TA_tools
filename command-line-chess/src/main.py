import random
import sys

from AI import AI
from Board import Board
from InputParser import InputParser

WHITE = True
BLACK = False
op_input = "op_input.txt"
AI_output = "AI_output.txt"



def askForPlayerSide():
    playerChoiceInput = input(
        "What side would you like to play as [wB]? ").lower()
    if 'w' in playerChoiceInput:
        print("You will play as white")
        return WHITE
    else:
        print("You will play as black")
        return BLACK


def askForDepthOfAI():
    depthInput = 2
    try:
        depthInput = int(input("How deep should the AI look for moves?\n"
                               "Warning : values above 3 will be very slow."
                               " [2]? "))
    except KeyboardInterrupt:
        sys.exit()
    except:
        print("Invalid input, defaulting to 2")
    return depthInput


def printCommandOptions():
    undoOption = 'u : undo last move'
    printLegalMovesOption = 'l : show all legal moves'
    randomMoveOption = 'r : make a random move'
    quitOption = 'quit : resign'
    moveOption = 'a3, Nc3, Qxa2, etc : make the move'
    options = [undoOption, printLegalMovesOption, randomMoveOption,
               quitOption, moveOption, '', ]
    print('\n'.join(options))


def printAllLegalMoves(board, parser):
    for move in parser.getLegalMovesWithNotation(board.currentSide, short=True):
        print(move.notation)


def getRandomMove(board, parser):
    legalMoves = board.getAllMovesLegal(board.currentSide)
    randomMove = random.choice(legalMoves)
    randomMove.notation = parser.notationForMove(randomMove)
    return randomMove


def makeMove(move, board):
    print("Making move : " + move.notation)
    board.makeMove(move)


def printPointAdvantage(board):
    print("Currently, the point difference is : " +
          str(board.getPointAdvantageOfSide(board.currentSide)))


def undoLastTwoMoves(board):
    if len(board.history) >= 2:
        board.undoLastMove()
        board.undoLastMove()


def startGame(board, playerSide, ai):
    parser = InputParser(board, playerSide)
    previous_count = 0
    count = 0
    while True:
        if len(open(op_input).readlines()) == 0:
            break
        else:
            print("Please Clear the op_input.txt first!")
    while True:

        if board.isCheckmate():
            if board.currentSide == playerSide:
                print("--------------------")
                print("AI: Today is a beautiful day!")
                print("--------------------")
            else:
                print("--------------------")
                print("AI: NOOOOOOOOOOOOOOOOOOOOOOOOOO!")
                print("--------------------")
            return

        if board.isStalemate():
            if board.currentSide == playerSide:
                print("--------------------")
                print("AI: Live together? See you next time")
                print("--------------------")
            else:
                print("--------------------")
                print("AI: Live together? See you next time")
                print("--------------------")
            return

        if board.currentSide == playerSide:
            # printPointAdvantage(board)
            move = None
            # command = input("It's your move."
            #                 " Type '?' for options. ? ")
            # if command.lower() == 'u':
            #     undoLastTwoMoves(board)
            #     continue
            # elif command.lower() == '?':
            #     printCommandOptions()
            #     continue
            # elif command.lower() == 'l':
            #     printAllLegalMoves(board, parser)
            #     continue
            # elif command.lower() == 'r':
            #     move = getRandomMove(board, parser)
            # elif command.lower() == 'exit' or command.lower() == 'quit':
            #     return
            # try:
            #     move = parser.parse(command)
            #     print("move: ", command)
            # except ValueError as error:
            #     print("%s" % error)
            #     continue
            # move = getRandomMove(board, parser)

            while True:
                previous_count = count
                count = len(open(op_input).readlines())
                if count - previous_count > 0:
                    with open(op_input) as f:
                        read_data = f.read().splitlines()
                        op_latest_input = read_data[-1]
                        print("--------------------")
                        print("BELOW IS YOUR MOVE")
                        print("--------------------")
                        move = parser.parse(op_latest_input)
                        f.closed                    
                    break
            makeMove(move, board)

        else:
            print("--------------------")
            print("AI: I will beat you!")
            print("--------------------")
            move = ai.getBestMove()
            move.notation = parser.notationForMove(move)
            makeMove(move, board)

            
            with open(AI_output, 'a+') as f:
                f.write(move.notation+'\n')
                f.closed                    
            # move = getRandomMove(board, parser)
        print(board)


def twoPlayerGame(board):
    parserWhite = InputParser(board, WHITE)
    parserBlack = InputParser(board, BLACK)
    while True:
        print()
        print(board)
        print()
        if board.isCheckmate():
            print("Checkmate")
            return

        if board.isStalemate():
            print("Stalemate")
            return

        # printPointAdvantage(board)
        if board.currentSide == WHITE:
            parser = parserWhite
        else:
            parser = parserBlack
        move = None
        command = input("It's your move, {}.".format(board.currentSideRep()) + \
                        " Type '?' for options. ? ")
        if command.lower() == 'u':
            undoLastTwoMoves(board)
            continue
        elif command.lower() == '?':
            printCommandOptions()
            continue
        elif command.lower() == 'l':
            printAllLegalMoves(board, parser)
            continue
        elif command.lower() == 'r':
            move = getRandomMove(board, parser)
        elif command.lower() == 'exit' or command.lower() == 'quit':
            return
        try:
            move = parser.parse(command)
        except ValueError as error:
            print("%s" % error)
            continue
        makeMove(move, board)


board = Board()

def main():
    try:
        if len(sys.argv) >= 2 and sys.argv[1] == "--two":
            twoPlayerGame(board)
        else:
            # playerSide = askForPlayerSide()
            playerSide = BLACK
            print()
            # aiDepth = askForDepthOfAI()
            aiDepth = 1
            opponentAI = AI(board, not playerSide, aiDepth)
            startGame(board, playerSide, opponentAI)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
