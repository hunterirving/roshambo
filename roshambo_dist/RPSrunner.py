from __future__ import division
from myRPSplayer import myRPSplayer
from opponent1 import opponent1
from opponent2 import opponent2
from opponent3 import opponent3

p1wins = 0
p2wins = 0
ties = 0

#Testing program that allows you to pit your lovingly crafted AI against a handful of dumb ones.
#Use this to prepare your AI for battle.

def simulateRound(yourInput, opponentInput):
    global p1wins, p2wins, ties
        
    validInput = ['R', 'P', 'S', '']
    
    if(yourInput not in validInput):
        raise ValueError("You made an invalid move. You played " + str(yourInput) + ". Valid inputs are 'R', 'P', and 'S'.")
    if(opponentInput not in validInput):
        raise ValueError("Your opponent made an invalid move. Your opponent played " + str(opponentInput) + ". Valid inputs are 'R', 'P', and 'S'.")
    
    if(yourInput == 'R'):
        if(opponentInput == 'R'):
            print "You played ROCK. Your opponent played ROCK. (TIE)"
            ties += 1
        elif(opponentInput == 'P'):
            print "You played ROCK. Your opponent played PAPER. (OPPONENT WON)"
            p2wins += 1
        elif(opponentInput == 'S'):
            print "You played ROCK. Your opponent played SCISSORS. (YOU WON)"
            p1wins += 1
    elif(yourInput == 'P'):
        if(opponentInput == 'R'):
            print "You played PAPER. Your opponent played ROCK. (YOU WON)"
            p1wins += 1
        elif(opponentInput == 'P'):
            print "You played PAPER. Your opponent played PAPER. (TIE)"
            ties += 1
        elif(opponentInput == 'S'):
            print "You played PAPER. Your opponent played SCISSORS. (OPPONENT WON)"
            p2wins += 1
    elif(yourInput == 'S'):
        if(opponentInput == 'R'):
            print "You played SCISSORS. Your opponent played ROCK. (OPPONENT WON)"
            p2wins += 1
        elif(opponentInput == 'P'):
            print "You played SCISSORS. Your opponent played PAPER. (YOU WON)"
            p1wins += 1
        elif(opponentInput == 'S'):
            print "You played SCISSORS. Your opponent played SCISSORS. (TIE)"
            ties += 1

def opponentSelect():
    choice = ''
    while not(choice == '1' or choice == '2' or choice == '3'):
        
        choice = raw_input("Choose your opponent: (1) always plays rock, (2) plays randomly, (3) counters your most frequently played move: ")
        print("")        
        if(choice == '1'):
            return opponent1()
        elif(choice == '2'):
            return opponent2()
        elif(choice == '3'):
            return opponent3()

player1 = myRPSplayer()
player2 = opponentSelect()
player1output = ''
player2output = ''

#modify this variable to change the number of rounds to simulate
upTo = 100

for x in range (0,upTo):
    temp = player1.playRound(player2output)
    player2output = player2.playRound(player1output)
    player1output = temp
    simulateRound(player1output, player2output)

print("\nOf " + str(upTo) + " rounds, you won " + str(p1wins) + " and your opponent won " + str(p2wins) + ". " + str(ties) + " rounds were ties.")
winrate = (p1wins/upTo)*100
print("Your winrate was " + str(winrate) + "%.")
opponentwinrate = (p2wins/upTo)*100
print("Your opponent's winrate was " + str(opponentwinrate) + "%.")

if(p1wins == p2wins):
    print("This match ended in a draw.\n")
elif(p1wins < p2wins):
    print("You lost this match.\n")
elif(p1wins > p2wins):
    print("You won this match!\n")
