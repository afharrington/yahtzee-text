import random
import os
import time
import rules
import scoring
import sys

def game(): 
    while True:
        round_num = 1
        all_scores = ['  ' for i in range(13)] + [0, 0]               
        bools_scores = bools(all_scores)
        while round_num < 14:
            all_scores = play_round(round_num, all_scores, bools_scores)
            bools_scores = bools(all_scores)
            round_num = round_num + 1
        game_score = scoring.final_score(all_scores)
        scoring.show_scorecard(all_scores)
        print('Your final score for this game is:', game_score)
        if game_score > int(current_hs):
            update_hs(game_score, 'highscores.txt') 
        else:
            print('\nThe high score is:', current_hs, 'played by', player_hs)
        if game_over() == True:
            print('\nGoodbye!')
            break 

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def load_hs(filename):
    with open(filename, 'r') as h:
        saved_score = h.readlines()
        for line in saved_score:
            score, name = line.split() 
        return int(score), name    

def update_hs(final_score, filename):
    print('Congrats! You have the new high score.\n')
    name = input('Enter your name: ')
    with open(filename, 'w') as h:
        h.write(str(final_score) + ' ' + name)       

# sets scoring category to True when filled
def bools(scores):
    bools = []
    for i in scores:
        if i == '  ':
            bools.append(False)
        else:
            bools.append(True)
    return bools

def play_round(rounds, scores, bools_scores):
    roll_num = 1
    kept_codes = []
    roll = [0,0,0,0,0]
    choice = []
    ubonus = 0
    ybonus = 0
    while roll_num < 4: 
        clear()
        print('Rolling...')
        time.sleep(.5)
        clear()
        print('ROUND:', rounds)
        print('ROLL:', roll_num)
        scoring.show_scorecard(scores)
        kept_bools = keep_bools(choice)
        roll = roll_dice(kept_bools, roll, choice)
        print('Dice: ', roll)
        print('Codes: [A, B, C, D, E]\n')
        while True:
            if roll_num < 3:
                print('[ABCDE]   Enter letter codes of dice to keep and roll again')
                print('    [F]   Roll ALL dice again\n')
            print(' [1-13]   Score dice by entering a category code') 
            print('    [R]   Review rules')          
            choice = input('> ').lower()            
            
            # if viewing rules
            if choice == 'r':
                rules.show_cheatsheet()
                print('ROUND:', rounds)
                print('ROLL:', roll_num)
                scoring.show_scorecard(scores)
                print('Dice: ', roll)
                print('Codes: [A, B, C, D, E]\n') 
                continue       
            # if selecting dice to keep
            elif set(choice).issubset(set('abcdef')) == True:     
                if roll_num == 3:
                    print('\nInvalid input. You must select a category to score.\n')
                elif confirm_dice(choice):
                    action = 'k'
                    break           
            # if scoring
            elif check_cat(choice, bools_scores, roll, scores) == True:
                if check_ybonus(roll, scores) == True:
                    scores[14] = scores[14] + 100         
                action = 's'
                break     
        # update scores or track keepers 
        if action == 's':
            cat = int(choice)
            cat_bool = scoring.valid(cat, roll)
            return scoring.score_dice(scores, roll, cat, cat_bool)
        else:
            kept_bools = keep_bools(choice)
            roll_num = roll_num + 1
        
# checks for yahtzee bonus
def check_ybonus(roll, scores):
    if scores[11] == 50 and [i for i in roll if roll.count(i) == 5]:
        print('Yahtzee Bonus!')
        return True

# validates category choice
def check_cat(category, bools, roll, scores):
    try:  
        if 0 < int(category) < 14:
            cat = int(category)
            if bools[cat-1] == True:
                print('Category taken! Try again.\n')         
            else: 
                if confirm_cat():
                    return True 
        else:
            print('\nThat category doesn\'t exist! Try again.\n')                  
    except ValueError:
        print('\nInvalid input. Try again.\n')  

# confirms category choice
def confirm_cat():
    while True:  
        print('\nOK to score round?\n[Y] Yes\n[N] No (Go Back)')
        confirm = input('> ')
        if confirm.lower() == 'y':
            return True
        elif confirm.lower() == 'n':
            return False
        else:
            print('Invalid input. Try again.\n')

# one roll
def keep_bools(kept_codes):
    kept_bools = []
    for i in ['a','b','c','d','e']:
        if i in kept_codes:
            kept_bools.append(True)
        else:
            kept_bools.append(False)
    return kept_bools   

def roll_dice(kept_bools, orig_roll, kept_dice): 
    new_dice = []
    for i in range(5):
        if kept_bools[i] == True:
            new_dice.append(orig_roll[i])
        else:
            new_dice.append(random.randint(1,6))
    return new_dice   

# confirms dice selection for keepers
def confirm_dice(selection):
    while True:
        if selection == 'f':
            print('\nRoll all dice again?\n[Y] Yes\n[N] No (Go Back)')
        else:
            print('\nKeep dice at these positions?  ' + selection.upper() + '\n[Y] Yes\n[N] No (Go Back)')
        confirm = input('> ').lower()
        if confirm == 'y':
            return True
        elif confirm == 'n':
            return False
        else:
            print('\nInvalid input. Try again.')

# returns True if roll meets category requirements
def game_over():
    while True:
        print('\nPlay again?\n[Y] Yes\n[N] No')
        play = input('> ').lower() 
        if play == 'n':
            return True
        elif play == 'y':
            return False    

if sys.version_info < (3, 0):
    print("Sorry! Yahtzee requires Python 3. Please try again.") 
    exit()

rules.read_rules()
current_hs, player_hs = load_hs('highscores.txt')
game()
