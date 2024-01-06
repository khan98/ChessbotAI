import ChessEngine as ce
import chess as ch

class Main:
    def __init__(self, chessSet=ch.chessSet):
        self.chessSet=chessSet
    #play human move
    def playerTurn(self):
        try:
            print(self.chessSet.legal_moves)
            print("""To undo your last move, type "undo".""")
            #get human move
            play = input("Your move: ")
            if (play=="undo"):
                self.chessSet.pop()
                self.chessSet.pop()
                self.playerTurn()
                return
            self.chessSet.push_san(play)
        except:
            self.playerTurn()
    def engineTurn(self, depth, color):
        engine = ce.Engine(self.chessSet, depth, color)
        self.chessSet.push(engine.optimal())
    #begin game
    def start(self):
        #get player's color
        color=None
        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        depth=None
        while(isinstance(depth, int)==False):
            depth = int(input("""Choose depth: """))
        if color=="b":
            while (self.chessSet.is_checkmate()==False):
                print("Let the engine think...")
                self.engineTurn(depth, ch.WHITE)
                print(self.chessSet)
                self.playerTurn()
                print(self.chessSet)
            print(self.chessSet)
            print(self.chessSet.outcome())    
        elif color=="w":
            while (self.chessSet.is_checkmate()==False):
                print(self.chessSet)
                self.playerTurn()
                print(self.chessSet)
                print("The engine is thinking...")
                self.engineTurn(depth, ch.BLACK)
            print(self.chessSet)
            print(self.chessSet.outcome())
        #reset board
        self.chessSet.reset
        #play again
        self.start()
#create an instance and start a game
newchessSet= ch.chessSet()
game = Main(newchessSet)
bruh = game.start()