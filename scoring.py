# check if roll fits category   
def valid(cat, roll):
    if cat in range(1,7) or cat == 13:
        return True           
    # 3 of a kind
    if cat == 7:
        if any([i for i in roll if roll.count(i) > 2]):
            return True
        else:
            return False                  
    # 4 of a kind  
    if cat == 8:
        if any([i for i in roll if roll.count(i) > 3]):
            return True
        else:
            return False           
    # full house
    if cat == 9:
        if any([i for i in roll if roll.count(i) == 2]) and any([i for i in roll if roll.count(i) == 3]):  
            return True
        else:
            return False           
 
    # small straight
    if cat == 10:
        x = list(set(roll)) 
        if len(x) == 4:
            if x in [list(range(1,5)), list(range(2,6)), list(range(3,7))]: 
                return True
            else:
                return False
        elif len(x) == 5:
            if list(range(1,5)) or list(range(2,6)) or list(range(3,7)) in x: 
                return True
            else: 
                return False
        else:
            return False 

    # large straight
    if cat == 11:
        x = list(set(roll)) 
        if x in [list(range(1,6)), list(range(2,7))]: 
            return True
        else: 
            return False    
    # yahtzee
    if cat == 12: 
        if any([i for i in roll if roll.count(i) == 5]):
            return True
        else:
            return False

# calculates points
def score_dice(scores, roll, cat, cat_bool):   
    if cat_bool == True:
        for i in range(1,7):
            if cat == i:
                points = roll.count(cat) * cat
                scores[cat-1] = points
        if cat == 7: 
            scores[cat-1] = sum(roll)
        elif cat == 8:
            scores[cat-1] = sum(roll)
        elif cat == 9:
            scores[cat-1] = 25
        elif cat == 10:
            scores[cat-1] = 30
        elif cat == 11: 
            scores[cat-1] = 40       
        elif cat == 12:
            scores[cat-1] = 50
        elif cat == 13: 
            scores[cat-1] = sum(roll)
    elif cat_bool == False:
        scores[cat-1] = 0
    return scores   

def show_scorecard(scores):
    scorecard = '''
Code  Upper Section
----  -------------
 1    |{:2}| Aces
 2    |{:2}| Twos
 3    |{:2}| Threes
 4    |{:2}| Fours
 5    |{:2}| Fives
 6    |{:2}| Sixes
 
      Lower Section
      -------------
 7    |{:2}| 3 of a kind
 8    |{:2}| 4 of a kind
 9    |{:2}| Full House (25 Pts)
 10   |{:2}| Small Straight (30 Pts)
 11   |{:2}| Large Straight (40 Pts)
 12   |{:2}| Yahtzee (50 Pts)
 13   |{:2}| Chance
 
      {:3}| Upper Section Bonus (35 Pts)
      {:3}| Yahtzee Bonus (100 Pts Each)

'''.format(*scores)
    print(scorecard)
    
def final_score(scores):
    if sum(scores[0:6]) > 62:
        scores[13] = 35
    for i in scores:
        if i == '  ':
            i = 0
    final = sum(scores[0:13])    
    return final
