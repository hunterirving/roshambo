import random

rockCount = 0
paperCount = 0
scissorsCount = 0

class opponent3():

    #Replace these fields
    creatorName = "Hunter"
    programName = "Wobuffet"
    
    #This function is called each round to determine your move for that round.
    #This function recieves as input a string containing your opponent's move from the last round.
    #In the first round of a match, input will contain an empty string as your opponent will not have yet made any moves.
    #You are allowed to create and call any additional functions you like.
    #You are allowed to create any local/global variables you like.
    #This function must return 'R', 'P', or 'S' as output.
    def playRound(self, input):
        global rockCount
        global paperCount
        global scissorsCount
        
        if(input == ''):
            return random.choice(['R','P','S'])
        elif(input == 'R'):
            rockCount += 1
        elif(input == 'P'):
            paperCount += 1
        elif(input == 'S'):
            scissorsCount += 1
        
        if(rockCount == paperCount and paperCount == scissorsCount):
            return random.choice(['R','P','S'])
        elif(rockCount == paperCount and rockCount > scissorsCount):
            return random.choice(['P','S'])
        elif(rockCount == scissorsCount and rockCount > paperCount):
            return random.choice(['P','R'])
        elif(paperCount == scissorsCount and paperCount > rockCount):
            return random.choice(['S','R'])
            
        elif(rockCount > paperCount and rockCount > scissorsCount):
            return 'P'
        elif(paperCount > rockCount and paperCount > scissorsCount):
            return 'S'
        elif(scissorsCount > rockCount and scissorsCount > paperCount):
            return 'R'
