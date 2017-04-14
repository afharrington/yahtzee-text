import os

def show_cheatsheet():
    clear()
    cheatsheet ='''
SCORECARD

Code  Category         Scoring
----  --------         -------
 1    Aces             Count & Add Only Aces
 2    Twos             Count & Add Only Twos
 3    Threes           Count & Add Only Threes
 4    Fours            Count & Add Only Fours
 5    Fives            Count & Add Only Fives
 6    Sixes            Count & Add Only Sixes
 

 7    3 of a kind      Add Total of All Dice
 8    4 of a kind      Add Total of All Dice
 9    Full House       3 of a Kind + 2 of a Kind (Score 25)
 10   Small Straight   Sequence of 4 (Score 30)
 11   Large Straight   Sequence of 5 (Score 40)
 12   Yahtzee          5 of the Same (Score 50)
 13   Chance           Add Total Of All Dice
 
      Upper Bonus      Score 35 if Upper Section > 62
      Yahtzee Bonus    Score 100 Per Additional Yahtzee
'''
    print(cheatsheet)
    while True:
        print('[C] Clear and return to game')
        if input('> ') == 'c':
            clear()
            break
    return False        
    
    
def read_rules():
    print('Read rules?\n[Y] Yes\n[N] No')
    action = input('> ').lower()
    if action == 'y':
        clear()
        print('''
YAHTZEE GAME RULES
-------------------------------------------------------------

The object of the game is to maximize your score in 13 rounds,
by filling in the scorecard categories below:

SCORECARD

Code  Category         Scoring
----  --------         -------
 1    Aces             Count & Add Only Aces
 2    Twos             Count & Add Only Twos
 3    Threes           Count & Add Only Threes
 4    Fours            Count & Add Only Fours
 5    Fives            Count & Add Only Fives
 6    Sixes            Count & Add Only Sixes
 

 7    3 of a kind      Add Total of All Dice
 8    4 of a kind      Add Total of All Dice
 9    Full House       3 of a Kind + 2 of a Kind (Score 25)
 10   Small Straight   Sequence of 4 (Score 30)
 11   Large Straight   Sequence of 5 (Score 40)
 12   Yahtzee          5 of the Same (Score 50)
 13   Chance           Add Total Of All Dice
 
      Upper Bonus      Score 35 if Upper Section > 62
      Yahtzee Bonus    Score 100 Per Additional Yahtzee

''')
        input('[Enter] To Continue')
        print('''
A round begins by rolling 5 dice:

Dice:  [5, 2, 6, 3, 6]
Codes: [A, B, C, D, E]

You may choose to score your dice, select dice to keep
for your next roll, or review the scoring rules above:

[ABCDE]   Enter letter codes of dice to keep and roll again
    [F]   Roll ALL dice again

 [1-13]   Score dice by entering a category code
    [R]   Review rules
    ''')    
        input('[Enter] To Continue')
        print('''
After your third roll, you must select a 
category to score your dice. If your dice do not meet the 
requirements of the category, a zero will be entered in 
that category.

Once a category has been filled, it cannot be used again.
If you score more than one Yahtzee, you will receive 
100 bonus points. You must still select another category
to score.

Scoring ends the round.     
''')
        input('[Enter] To Play')        
        clear()
        
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
