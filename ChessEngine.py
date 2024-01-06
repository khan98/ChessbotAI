import chess as ch
import random as rand

class Engine:

    def __init__(self, set, maxDepth, color): #self indicates player, set indicates board
        self.set=set
        self.color=color
        self.maxDepth=maxDepth
    #Gets the optimal or "best" move
    def optimal(self):
        return self.engine(None, 1)
    def evaluation(self):
        comp = 0
        for i in range(64):
            comp+=self.berliner(ch.SQUARES[i])
        comp+=self.checkmate()+self.opening()+0.001*rand.random()
        return comp
    def checkmate(self):
        if(self.set.legal_moves.count()==0):
            if(self.set.turn == self.color):
                return -999
            else:
                return 999
        else:
            return 0
    def opening(self):
        if(self.set.fullmove_number<10):
            if(self.set.turn==self.color):
                return 1/30*self.set.legal_moves.count()   
            else:
                return -1/30*self.set.legal_moves.count()   
        else:
            return 0 

    

    #Takes a square as input and returns the corresponding Berliner's system value of it's resident
    def berliner(self, square):
        value=0
        if(self.set.piece_type_at(square) == ch.PAWN):
            value=1
        elif(self.set.piece_type_at(square) == ch.ROOK):
            value=5.1
        elif(self.set.piece_type_at(square) == ch.BISHOP):
            value=3.33
        elif(self.set.piece_type_at(square) == ch.KNIGHT):
            value=3.2
        elif(self.set.piece_type_at(square) == ch.QUEEN):
            value=8.8
        if(self.set.color_at(square)!=self.color):
            return -value
        else:
            return value

    def engine(self, candidate, depth):
        if(depth == self.maxDepth or self.set.legal_moves.count()==0):
            return self.evaluation()
        else:
            #get a list of legal moves of the current position
            moveList = list(self.set.legal_moves)
            newCandidate=None
            if(depth % 2 != 0):
                newCandidate=float("-infinity")
            else:
                newCandidate=float("infinity")
            for i in moveList:
                #Play the move i
                self.set.push(i)
                #Return value of move
                value = self.engine(newCandidate, depth+1)
                #Minmax without alpha-beta pruning
                if(value > newCandidate and depth % 2 != 0):
                    newCandidate=value
                    if(depth==1):
                        move=i
                #Minimize player's turn
                if(value < newCandidate and depth % 2 != 0):
                    newCandidate=value 
                #Alpha-beta pruning cuts:
                #if previous move was made by the player
                if (candidate != None and value < candidate and depth % 2 == 0):
                    self.set.pop()
                    break
                elif (candidate != None and value > candidate and depth % 2 != 0):
                    self.set.pop()
                    break
                self.set.pop()
        if (depth > 1):
            #return value of the node in the tree
            return newCandidate
        else:
            return move