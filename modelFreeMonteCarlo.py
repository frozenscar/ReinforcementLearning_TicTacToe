from collections import defaultdict
import random


class TicTacToe:
    def __init__(self):
        self.Board = ''

    def playAgainstHuman(self,agent,epsilon=0):
        self.Board = "---------"
        print("Go first.\n 1.Yes \n2.No \n")
        ip = int(input())
        curPlayer = 0
        player = 'O'
        if(ip == 1):
            self.DisplayBoard(self.Board)
            player = 'X'
            p = int(input())
            if self.Board[p-1]=="-" and p <10:
               self.Board =  self.playMove(p-1,"X",self.Board)
            else:print("invalid move")
            curPlayer = 0

        while(self.GameStatus(self.Board) and '-' in self.Board):
            if(curPlayer%2==0):
                pl = 'X'
                if(player)=='X':
                    pl = 'O'
                pos = agent.Policy(self.Board, epsilon)
                self.Board = self.playMove(pos, pl, self.Board)
                curPlayer = 1
                self.DisplayBoard(self.Board)
            else:
                curPlayer = 0
                pos = int(input())-1
                if self.Board[pos] == "-" and pos < 10:
                    self.Board = self.playMove(pos, player, self.Board)
                else:
                    print("invalid move")
                    curPlayer=1


                self.DisplayBoard(self.Board)


        if (self.GameStatus(self.Board) == False):
            if (curPlayer == 1):
                agent.Result(1)
                print('Agent Won!')
            else:
                agent.Result(-1)
                print('you Won!')
        else:
            print('Draw!')





    def startGame(self,agent1,agent2,epsilon=0):


        self.Board = "---------"

        curPlayer = 'X'
        while(self.GameStatus(self.Board) and '-' in self.Board):

            if(curPlayer == 'X'):
                pos = agent1.Policy(self.Board,epsilon)
                self.Board = self.playMove(pos,curPlayer,self.Board)
                curPlayer='O'
                self.DisplayBoard(self.Board)

            else:
                pos = agent2.Policy(self.Board,epsilon)
                self.Board = self.playMove(pos, curPlayer, self.Board)
                self.DisplayBoard(self.Board)
                curPlayer=('X')

        if(self.GameStatus(self.Board)==False):
            if(curPlayer=='X'):
                agent2.Result(1)
                agent1.Result(-1)
                print('O Won')
            else:
                agent1.Result(1)
                agent2.Result(-1)
                print('X Won')
        else:
            agent1.Result(0)
            agent2.Result(0)


    def playMove(self,pos,player,Board):
        Board = list(Board)

        if Board[pos]=='-':
            Board[pos]=player
        return "".join(Board)

    def DisplayBoard(self,Board):
        c=0
        for i in range(3):
            for j in range(3):
                print(Board[c],end=" ")
                c=c+1
            print("\n")

    def GameStatus(self,state):
        # returns True if there are playable Moves
        for i in range(3):

            if(state[0+i]==state[3+i]==state[6+i] and state[0+i] != '-'):
                return False
        for i in range(3):
            if(state[0+3*i]==state[1+3*i]==state[2+3*i] !='-'):
                return False
        if(state[0]==state[4]==state[8] !='-'):
            return False
        if(state[2]==state[4]==state[6] !='-'):
            return False
        return True

class Agent:
    def __init__(self,readActionValues=0):

        #gives possible actions for a state
        self.psble_actions = defaultdict(lambda : -1)


        if readActionValues !=0 :
            self.readActionValues(readActionValues)

        self.episode =[]

    def Policy(self,state,epsilon=0):
        if self.psble_actions[state]== -1:
            possibleActions = []
            for c in range(len(state)):
                if state[c]=='-':
                    possibleActions.append([c,0,0])
            self.psble_actions[state] = possibleActions


        rand = random.random()
        if(rand <= epsilon):
            print("choosing Random")
            ans1 = random.choice(self.psble_actions[state])
            ans1[2]+=1
            self.episode.append([state,ans1[0]])
            return ans1[0]
        else:
            mx = -99999
            for i in self.psble_actions[state]:
                if i[1]>mx:
                    mx = i[1]
                    ans = i[0]
                    inc = i
            inc[2]+=1
            self.episode.append([state, ans])
            return ans


    def Result(self,Reward):
        self.updateActionValues(Reward)
        self.episode=[]

    def updateActionValues(self,Reward):
        l = len(self.episode)
        c=1
        for i in self.episode:
            #i list of [states,actions]
            for j in self.psble_actions[i[0]]:
                #j list of [possibleAction, actionValue]s

                if j[0]==i[1]:
                    j[1]+= 1/j[2]*((0.9**(l-c)*Reward) - j[1])

    def saveActionValues(self,name):
        name = str(name)
        with open("ActionValues"+name+".txt",mode="w") as f:
            for i in self.psble_actions:
                f.write(i + " ")
                for j in self.psble_actions[i]:
                    f.write(str(j[0])+" "+str(round(j[1],2))+" "+str(j[2])+" ")
                f.write("\n")


    def readActionValues(self,name):
        name = str(name)

        with open("ActionValues"+name+".txt",'r') as f:
            line = f.readline()
            while(line):
                line = line.split()
                line1 = line[1:]
                self.psble_actions[line[0]] = []
                for i in range(int(len(line1)/3)):
                    self.psble_actions[line[0]].append([int(line1[3*i]),float(line1[3*i + 1]),int(line1[3*i+2])])
                line = f.readline()








agent3 = Agent(3)
game = TicTacToe()
'''
for i in range(100000):
    epsilon = 0
    if i<1000:
        epsilon = 0.5
    if i<25000:
        epsilon = 0.15
    else:
        epsilon = 0.07
    game.startGame(agent1,agent2,epsilon)
'''
game.playAgainstHuman(agent3)

#agent1.saveActionValues(1)
#agent2.saveActionValues(2)















