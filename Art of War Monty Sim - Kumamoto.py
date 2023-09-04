import random

""" ***** FULL SIM *****
Written by "TheOriginalOz"
https://github.com/TheOriginalOz

For Kumamoto
    Assuming one would try to fill row 1, then row 4 with two dice, then fill row 2/3, then fill row 4 with any.
"""
""" Value notes
1 = 1 sword
2 = 2 swords
3 = 3 swords
4 = Archer
5 = Knight
6 = Daimyo
"""

def main():
    Sim_count = 0
    Hit = 0
    ROLL_RESULT = []
    swords = [1, 2, 3]
    while Sim_count < 10000000:

        # Initialise variables
        Dice_count = [7]

        # For each row on card, 1 = completed
        Rows = [0] * 4

        #Roll first set of dice
        roll(ROLL_RESULT, Dice_count) 
        #ROLL_RESULT = [6, 6, 6, 6, 6, 6, 6]

        #Try to fill first row
        if check1(ROLL_RESULT, Dice_count, Rows, swords) == 1:
            # Try to fill remaining rows
            while dice_left(Rows, Dice_count) == 1:
                filterer(ROLL_RESULT, Dice_count, Rows, swords)
                if 0 not in Rows:
                    Hit += 1
                    Sim_count += 1
                    break
            else:
                Sim_count += 1        

        # Try to fill row 4
        elif check4(ROLL_RESULT, Dice_count, Rows, swords) == 1:
            # Try to fill remaining rows
            while dice_left(Rows, Dice_count) == 1:
                filterer(ROLL_RESULT, Dice_count, Rows, swords)
                if 0 not in Rows:
                    Hit += 1
                    Sim_count += 1
                    break
            else:
                Sim_count += 1
            # Didn't get row 1 or 4, reset roll

    hit_rate = Hit / Sim_count * 100
    print("Completion rate for Kumamoto is: " + str(format(hit_rate, ".2f")), "%", sep="")

    """ *** Here be functions *** """

# Rolls a fresh set of dice
def roll(ROLL_RESULT, Dice_count):
    ROLL_RESULT.clear()
    for x in range(Dice_count[0]):
        ROLL_RESULT.append(random.randrange(1, 7, 1))

# Checks for double daimyo
def check1(ROLL_RESULT, Dice_count, Rows, swords):
    roll_check = 0
    if Dice_count[0] >= 2:
        for x in ROLL_RESULT:
            if x == 6:
                roll_check += 1
                if roll_check >= 2:
                    Dice_count[0] = Dice_count[0] - 2
                    Rows[0] = 1
                    return 1
    else:
        return 0

# Checks for Archer in roll, otherwise lose a dice
def check2(ROLL_RESULT, Dice_count, Rows, swords):
    if 4 in ROLL_RESULT:
        Dice_count[0] = Dice_count[0] - 1
        Rows[1] = 1
        return 1

# Checks for Kinght in roll, otherwise lose a dice
def check3(ROLL_RESULT, Dice_count, Rows, swords):
    if 5 in ROLL_RESULT:
        Dice_count[0] = Dice_count[0] - 1
        Rows[2] = 1
        return 1

# Checks for 4 swords total across max of 2 dice
def check4(ROLL_RESULT, Dice_count, Rows, swords):
    sword_count = 0
    if Dice_count[0] >= 2:
        for x in ROLL_RESULT:
            if x == swords[1] or x == swords[2]:
                sword_count += x
                if sword_count >= 4:
                    Dice_count[0] = Dice_count[0] - 2
                    Rows[3] = 1
                    return 1
                else:
                    return 0
    else:
        return 0
    
# Last chance saloon, 4 swords on 3 dice
def check5(ROLL_RESULT, Dice_count, Rows, swords):
    sword_count = 0
    dice = 0
    for x in ROLL_RESULT:
        if x == swords[1] or x == swords[2] or x == swords[0]:
            sword_count += x
            dice += 1
            if sword_count >= 4 and dice <= 3:
                Dice_count[0] = Dice_count[0] - dice
                Rows[3] = 1
                return 1
    
def filterer(ROLL_RESULT, Dice_count, Rows, swords):
    roll(ROLL_RESULT, Dice_count)
    if Rows[0] != 1:
        if check1(ROLL_RESULT, Dice_count, Rows, swords) == 1:
            return 0
    if Rows[3] != 1:
        if check4(ROLL_RESULT, Dice_count, Rows, swords) == 1:
            return 0
    if Rows[1] != 1:
        if check2(ROLL_RESULT, Dice_count, Rows, swords) == 1:
            return 0
    if Rows[2] != 1:
        if check3(ROLL_RESULT, Dice_count, Rows, swords) == 1:
            return 0
    if Rows[3] != 1:
        if check5(ROLL_RESULT, Dice_count, Rows, swords) == 1:
            return 0
        else:
            Dice_count[0] = Dice_count[0] - 1
    else:
        Dice_count[0] = Dice_count[0] - 1

# Checks if there are enough dice left to continue
def dice_left(Rows, Dice_count):
    mindice = 6
    if Rows[0] == 1:
        mindice -= 2
    if Rows[1] == 1:
        mindice -= 1
    if Rows[2] == 1:
        mindice -= 1
    if Rows[3] == 1:
        mindice-=2
    if Dice_count[0] < mindice:
        return 0
    else:
        return 1

if __name__ == "__main__":
    main()