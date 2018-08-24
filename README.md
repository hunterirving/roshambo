# roshambo

## _The year is 20XX, and Rock-Paper-Scissors has become a multi-national spectator sport._

<img src="https://github.com/hunterirving/roshambo/blob/master/photo-rock_paper_scissors2.jpg">

Since The National Rock-Paper-Scissors Association _(NRPSA)_ legalized the introduction of AI combatants, bots dominate the professional leagues.



For humans, the new challenge lies in __programming the perfect bot.__

<br>

## _The Minor Leagues_

A popular pasttime among diehard RPS fans has become hosting un-official local tournaments - pitting their own AIs against each other, starry-eyed and hopeful that they might one day make it to the majors.

Hunter Irving's ___roshambo___ quickly emerged as the de-facto standard for running a local.

```python
class myRPSplayer():

    #Replace these fields
    creatorName = "Creator Name"
    programName = "Program Name"

    #This function is called each round to determine your move for that round.
    #This function recieves as input a string containing your opponent's move from the last round.
    #In the first round of a match, "input" will contain an empty string.
    #You are allowed to create and call any additional functions you like.
    #You are allowed to create any local/global variables you like.
    #This function must return 'R', 'P', or 'S' as output.
    def playRound(self, input):
        return 'P'
```

As the Tournament Organizer (TO), distribute ___roshambo_dist___ to each of your entrants.

Entrants can modify ___myRPSplayer.py___ to write their own AI, then submit it to you for entry into the tournament.

Along with several dummy AIs, ___RPSrunner.py___ is supplied to entrants, allowing them to simulate a match between two AI combatants.

<img src="testin">

When all entrants have submitted thier AIs, place them into ___roshambo_tournament___ and run the ___RPSrunner.py___ file located there.

The Final Results should be available after just a few moments.

<img src="winner">

## _Something... Sinister.......?_

In rare cases, AI combatants have been shown to _"gain sentience"_ and _"challenge their creator to one final battle to determine the fate of the world"._

<img src="">

However, this is ___NOT___ the intended functionality of the software, and Hunter Irving takes ___NO RESPONSIBILITY___ for damages to hardware, software, ego, or perception of reality caused by the use or misuse of the aforementioned software.
