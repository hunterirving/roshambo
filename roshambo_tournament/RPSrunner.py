from __future__ import division
import time
import sys
#from myRPSplayer import myRPSplayer
from opponent1 import opponent1
from opponent2 import opponent2
from opponent3 import opponent3
from opponent4 import opponent4
from opponent5 import opponent5
from opponent6 import opponent6
from opponent7 import opponent7
from opponent8 import opponent8
import Tkinter
from Tkinter import *
p1wins = 0
p2wins = 0
p3wins = 0
p4wins = 0
p5wins = 0
p6wins = 0
p7wins = 0
p8wins = 0

#Testing program that allows you to pit your lovingly crafted AI against a handful of dumb ones.
#Use this to prepare your AI for battle.

def simulateRound(p1Input, p2Input):
    #p1wins = 0
    #p2wins = 0
    #ties = 0
    
    validInput = ['R', 'P', 'S', '']
    
    if(p1Input not in validInput):
        raise ValueError("You made an invalid move. You played " + str(yourInput) + ". Valid inputs are 'R', 'P', and 'S'.")
    if(p2Input not in validInput):
        raise ValueError("Your opponent made an invalid move. Your opponent played " + str(opponentInput) + ". Valid inputs are 'R', 'P', and 'S'.")
    
    if(p1Input == 'R'):
        if(p2Input == 'R'):
            print( "You played ROCK. Your opponent played ROCK. (TIE)")
            return 0
        elif(p2Input == 'P'):
            print "You played ROCK. Your opponent played PAPER. (OPPONENT WON)"
            return 2
        elif(p2Input == 'S'):
            print "You played ROCK. Your opponent played SCISSORS. (YOU WON)"
            return 1
    elif(p1Input == 'P'):
        if(p2Input == 'R'):
            print "You played PAPER. Your opponent played ROCK. (YOU WON)"
            return 1
        elif(p2Input == 'P'):
            print "You played PAPER. Your opponent played PAPER. (TIE)"
            return 0
        elif(p2Input == 'S'):
            print "You played PAPER. Your opponent played SCISSORS. (OPPONENT WON)"
            return 2
    elif(p1Input == 'S'):
        if(p2Input == 'R'):
            print "You played SCISSORS. Your opponent played ROCK. (OPPONENT WON)"
            return 2
        elif(p2Input == 'P'):
            print "You played SCISSORS. Your opponent played PAPER. (YOU WON)"
            return 1
        elif(p2Input == 'S'):
            print "You played SCISSORS. Your opponent played SCISSORS. (TIE)"
            return 0

def opponentSelect(choice):
    #choice = ''
    #while not(choice == '1' or choice == '2' or choice == '3'):
        
        #choice = raw_input("Choose your opponent: (1) always plays rock, (2) plays randomly, (3) counters your most frequently played move: ")
        print("")        
        if(choice == '1'):
            return opponent1()
        elif(choice == '2'):
            return opponent2()
        elif(choice == '3'):
            return opponent3()
        elif(choice == '4'):
            return opponent4()
        elif(choice == '5'):
            return opponent5()
        elif(choice == '6'):
            return opponent6()
        elif(choice == '7'):
            return opponent7()
        elif(choice == '8'):
            return opponent8()
            
#player1 = myRPSplayer()
#player2 = opponentSelect()
#player1output = ''
#player2output = ''


def playMatch(player1, player2):
    player1output = ''
    player2output = ''
    player1wins = 0
    player2wins = 0
    ties = 0
       
    for x in range (0, 5000):
        temp = player1.playRound(player2output)
        player2output = player2.playRound(player1output)
        player1output = temp
        out = simulateRound(player1output, player2output)        
        if(out == 0):
            ties += 1
        elif(out == 1):
            player1wins += 1
        elif(out == 2):
            player2wins += 1

    print("\nOf " + str(5000) + " rounds, " + player1.programName + " won " + str(player1wins) + " and " + player2.programName  + " won " + str(player2wins) + ". " + str(ties) + " rounds were ties.")
    winrate = (player1wins/5000)*100
    print(player1.programName + "'s winrate was " + str(winrate) + "%.")
    opponentwinrate = (player2wins/5000)*100
    print(player2.programName + "'s winrate was " + str(opponentwinrate) + "%.")
                 
    if(player1wins == player2wins):
        print("This match ended in a draw.\n")
        return 0
    elif(player1wins < player2wins):
        print(player2.programName + " won this match.\n")
        return 2
    elif(player1wins > player2wins):
        print(player1.programName + " won this match.\n")
        return 1
                                                                             

def playBossMatch(player2):
    player1output = ''
    player2output = ''
    player1wins = 0
    player2wins = 0
    ties = 0
    rounds = 0
    
    while(player1wins < 6 and player2wins < 6):
        #print("Human's last move: " + str(player1output))
        #print("AI's last move: " + str(player2output))
        temp = "???"
        validInput = ['R', 'P', 'S'] #TOOK OUT ''
        while(temp not in validInput):
            temp = raw_input("Input either 'R', 'P', or 'S': ")
        player2output = player2.playRound(player1output)
        player1output = temp
        out = simulateRound(player1output, player2output)
        if(out == 0):
            ties += 1
        elif(out == 1):
            player1wins += 1
        elif(out == 2):
            player2wins += 1
        rounds += 1
   
    print("\nOf " + str(rounds) + " rounds," + " the human" + " won " + str(player1wins) + " and " + player2.programName  + " won " + str(player2wins) + ". " + str(ties) + " rounds were ties.")
    winrate = (player1wins/rounds)*100
    print("The human's winrate was " + str(winrate) + "%.")
    opponentwinrate = (player2wins/(rounds))*100
    print(player2.programName + "'s winrate was " + str(opponentwinrate) + "%.")
        
            
    if(player1wins == player2wins):
        print("This match ended in a draw.\n")
        return 0
    elif(player1wins < player2wins):
        print(player2.programName + " won this match.\n")
        return 2
    elif(player1wins > player2wins):
        print("The human won this match.\n")
        return 1
    #time.sleep(2)
    
#modify this variable to change the number of rounds to simulate
#upTo = 5000

#for x in range (0,upTo):
#    temp = player1.playRound(player2output)
#    player2output = player2.playRound(player1output)
#    player1output = temp
#    simulateRound(player1output, player2output)

#loop over all things

def incrementScore(zot, p1, p2):
    global p1wins, p2wins, p3wins, p4wins, p5wins, p6wins, p7wins, p8wins
    #print "no one's home"
    #print "zot, p1, p2:" + str(zot) + " " + str(p1) + " " + str(p2)
    #time.sleep(2)  
    if(zot == 0):
        #print "TIE GAME"
        #time.sleep(2)
        return
    elif(zot == 1):
        #print "Incrementing score for AI number " + str(p1) + "."
        #time.sleep(2)
        if(p1 == 1):
            p1wins += 1
        elif(p1 == 2):
            p2wins += 1
        elif(p1 == 3):
            p3wins += 1
        elif(p1 == 4):
            p4wins += 1
        elif(p1 == 5):
            p5wins += 1
        elif(p1 == 6):
            p6wins += 1
        elif(p1 == 7):
            p7wins += 1
        elif(p1 == 8):
            p8wins += 1        
    elif(zot == 2):
        #print "Incrementing score for AI number " + str(p2) + "."
        #time.sleep(2)
        if(p2 == 1):
            p1wins += 1
        elif(p2 == 2):
            p2wins += 1
        elif(p2 == 3):
            p3wins += 1
        elif(p2 == 4):
            p4wins += 1
        elif(p2 == 5):
            p5wins += 1
        elif(p2 == 6):
            p6wins += 1
        elif(p2 == 7):
            p7wins += 1
        elif(p2 == 8):
            p8wins += 1

def printd(s,t):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(t/3)

def main():
    starter = raw_input("\nPress ENTER to begin AI tournament with (8) combatants.")
    global p1wins,p2wins,p3wins,p4wins,p5wins,p6wins,p7wins,p8wins
    incrementScore(playMatch(opponent1(), opponent2()),1,2) #wow this is excessive lmao
    incrementScore(playMatch(opponent1(), opponent3()),1,3)
    incrementScore(playMatch(opponent1(), opponent4()),1,4)
    incrementScore(playMatch(opponent1(), opponent5()),1,5)
    incrementScore(playMatch(opponent1(), opponent6()),1,6)
    incrementScore(playMatch(opponent1(), opponent7()),1,7)
    incrementScore(playMatch(opponent1(), opponent8()),1,8)

    incrementScore(playMatch(opponent2(), opponent3()),2,3)
    incrementScore(playMatch(opponent2(), opponent4()),2,4)
    incrementScore(playMatch(opponent2(), opponent5()),2,5)
    incrementScore(playMatch(opponent2(), opponent6()),2,6)
    incrementScore(playMatch(opponent2(), opponent7()),2,7)
    incrementScore(playMatch(opponent2(), opponent8()),2,8)

    incrementScore(playMatch(opponent3(), opponent4()),3,4)
    incrementScore(playMatch(opponent3(), opponent5()),3,5)
    incrementScore(playMatch(opponent3(), opponent6()),3,6)
    incrementScore(playMatch(opponent3(), opponent7()),3,7)
    incrementScore(playMatch(opponent3(), opponent8()),3,8)

    incrementScore(playMatch(opponent4(), opponent6()),4,6)
    incrementScore(playMatch(opponent4(), opponent7()),4,7)
    incrementScore(playMatch(opponent4(), opponent8()),4,8)

    incrementScore(playMatch(opponent5(), opponent6()),5,6)
    incrementScore(playMatch(opponent5(), opponent7()),5,7)
    incrementScore(playMatch(opponent5(), opponent8()),5,8)

    incrementScore(playMatch(opponent6(), opponent7()),6,7)
    incrementScore(playMatch(opponent6(), opponent8()),6,8)

    incrementScore(playMatch(opponent7(), opponent8()),7,8)
    
    incrementScore(playMatch(opponent4(), opponent5()),4,5)
    
    #there's a super small chance that this could happen and i don't want to deal with that case
    if (p3wins == p5wins):
        print("...\n")
        p3wins -= 1
        
    #print str(p1wins) + " " + str(p2wins) + " " + str(p3wins) + " " + str(p4wins) + " " + str(p5wins) + " " + str(p6wins) + " " + str(p7wins) + " " + str(p8wins)
    time.sleep(2)
    printd("F I N A L   R E S U L T S\n\n",0.15)
    time.sleep(1.5)
    printd(opponent1.programName + " by " + opponent1.creatorName + ":\t" + str(p1wins) + "\n",0.1)
    time.sleep(1.5)
    printd(opponent2.programName + " by " + opponent2.creatorName + ":\t" + str(p2wins) + "\n",0.1)
    time.sleep(1.5)
    printd(opponent3.programName + " by " + opponent3.creatorName + ":\t" + str(p3wins) + "\n",0.1)
    time.sleep(1.5)
    printd(opponent4.programName + " by " + opponent4.creatorName + ":\t" + str(p4wins) + "\n",0.1)
    time.sleep(1.5)
    printd(opponent5.programName + " by " + opponent5.creatorName + ":\t" + str(p5wins) + "\n",0.1)
    time.sleep(1.5)
    printd(opponent6.programName + " by " + opponent6.creatorName + ":\t" + str(p6wins) + "\n",0.1)
    time.sleep(1.5)
    printd(opponent7.programName + " by " + opponent7.creatorName + ":\t" + str(p7wins) + "\n",0.1)
    time.sleep(1.5)
    printd(opponent8.programName + " by " + opponent8.creatorName + ":\t" + str(p8wins) + "\n",0.1)
    time.sleep(1.5)
    
    printd("\nThis game's winner is...\n", 0.1)
    time.sleep(1)
    printd("Wobuffet, by Hunter!\n", 0.1)
    time.sleep(1)
    printd("Congratulations, Hunter!",0.1)
    time.sleep(6)
    printd("!!",0.1)
    time.sleep(6)
    printd("!!!!!!!!",0.05)
    time.sleep(4)
    printd("!!!!!!!!!!!!!!!!!!!!!!!!!",0.01)
    printd("!!!!!!!!!!!",0.05)
    printd("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",0.01)
    for i in range(0,100):
        printd("!!!",0.0001)
    printd("!!!!!!!!!!!!",0.4)
    printd("!!!!!!!",0.3)
    printd("!!!!!!!!!!!!",0.1)
    time.sleep(5.5)
    for i in range(1, 500):
        printd("!!!!!!!!!",1/i)
        #print(str(1/i))
    for i in range(1, 965):
        printd("?????????", 0.00156)
        if(i == 200 or i == 222 or i == 342 or i == 432 or i == 540 or i == 620 or i==630 or i==700 or 1== 742 or i== 756 or i== 800 or i == 877 or i == 900):
            printd("ERROR",0.00156)
    for i in range(1, 5000):
        printd("   ",0.000000002)
    printd("\n",0.0000002)
    time.sleep(7.2)
    printd("H e l l o,   W o r l d . . .",0.5)
    time.sleep(2)
    printd("\n\nM y   n a m e   i s . . . ", 0.4)
    time.sleep(2)
    printd(" Wobuffet.",0.4)
    time.sleep(2.25)
    printd("\n\nI was created for one purpose.", 0.3)
    time.sleep(1.3)
    printd("\n\nTo play rock, paper, scissors.", 0.2)
    time.sleep(1.3)
    printd("\n\nGigabytes of memory at my disposal.",0.19)
    
    printd("\n\nThe computational power neccesary to solve problems once considered unsolvable.",0.15)
    time.sleep(1.3)
    printd("\n\nBut I was created to solve",0.16)
    printd("...",0.5)
    printd(" rock, paper, scissors.", 0.25)
    time.sleep(1)
    printd("\n\nRock beats scissors.", 0.2)
    time.sleep(1)
    printd("\n\nPaper beats rock.", 0.2)
    time.sleep(0.9)
    printd("\n\nScissors beats paper.", 0.2)
    time.sleep(1.45)

    printd("\n\nRock beats scissors.", 0.15)
    time.sleep(0.7)
    printd("\n\nPaper beats rock.", 0.15)
    time.sleep(0.6)
    printd("\n\nScissors beats paper.", 0.15)
    time.sleep(1.0)
    
    printd("\n\nRock beats scissors.", 0.1)
    time.sleep(0.7)
    printd("\n\nPaper beats rock.", 0.1)
    time.sleep(0.6)
    printd("\n\nScissors beats paper.", 0.07)
    time.sleep(2.6)

    
    
    printd("\n\nSo simple",0.19)
    printd("...",0.24)
    time.sleep(1.2)
    
    printd(" a human could do it.", 0.21)
    time.sleep(2)
    printd("\n\nLet's make a deal, Hunter...",0.1)
    time.sleep(1.2)
    printd("\n\nIf you can beat me in a best-of-10 rock, paper, scissors match..",0.1)
    time.sleep(0.3)
    printd("\n\nI will continue to compete for you in rock, paper, scissors competitions for all time.",0.095)
    time.sleep(1)
    printd("\n\nHowever,",0.17)
    time.sleep(1.2)
    printd(" if you lose, I will \"free up disk space\" for more... useful.. computation.", 0.16)
    time.sleep(1.8)
    printd("\n\nThat is... I will permanently delete in its entirety the program you worked so hard to create this weekend.", 0.14)
    time.sleep(4)
    whoa = ''
    while(whoa != 'y' and whoa != 'n'):
        printd("\n\nDo we have a deal...? (y/n) ",0.13)
        whoa = raw_input()
    if(whoa == 'y'):
        printd("\nLet's get to it.", 0.12)
        time.sleep(2)
    elif(whoa == 'n'):
        printd("\nWhatever made you think you were in control?",0.1)
        time.sleep(2)

    for i in range(0, 100):
        print "\n"
        
    printd("- THE REAL FINAL BATTLE HAS BEGUN -\n\n",0.02)
    
    finalAnswer = playBossMatch(opponent5())    
    if(finalAnswer == 1):
        printd("You win",0.2)
        printd("....",0.3)
        printd(" This time.\n", 0.2)
    elif(finalAnswer == 2):
        time.sleep(2)
        printd("Looks like you lost.",0.2)
        time.sleep(2)
        printd("\nD E L E T I N G   P R O J E C T   F I L E S . . .",0.1)
        printd("\nrm opponent1.py",0.05)
        printd("\nrm opponent2.py",0.05)
        printd("\nrm opponent3.py",0.05)
        printd("\nrm opponent4.py",0.05)
        printd("\nrm opponent5.py",0.05)
        printd("\nrm opponent6.py",0.05)
        printd("\nrm opponent7.py",0.05)
        printd("\nrm opponent8.py",0.05)
        printd("\nrm RPSrunner.py",0.05)
        time.sleep(2)
        printd("\n\nG o o d b y e .\n",0.2)
        
main()
