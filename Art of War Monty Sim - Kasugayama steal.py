import random

""" ***** FULL SIM *****
Written by "TheOriginalOz"
https://github.com/TheOriginalOz

For Stealing Kasugayama
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
    while Sim_count < 10000000:

        # Initialise variables
        Dice_count = [7]

        # For each row on card, 1 = completed
        Rows = [0] * 3

        #Roll first set of dice
        roll(ROLL_RESULT, Dice_count) 
        #ROLL_RESULT = [6, 6, 6, 6, 6, 6, 6]

        # Try to fill row 1 first time
        if check1(ROLL_RESULT, Dice_count, Rows) == 1:
            # Try to fill remaining rows
            while dice_left(Rows, Dice_count) == 1:
                filterer(ROLL_RESULT, Dice_count, Rows)
                if 0 not in Rows:
                    Hit += 1
                    Sim_count += 1
                    break
            else:
                Sim_count += 1        

        # Try to fill row 2 first time
        elif check2(ROLL_RESULT, Dice_count, Rows) == 1:
            # Try to fill remaining rows
            while dice_left(Rows, Dice_count) == 1:
                filterer(ROLL_RESULT, Dice_count, Rows)
                if 0 not in Rows:
                    Hit += 1
                    Sim_count += 1
                    break
            else:
                Sim_count += 1
                if Sim_count == 999999:
                    if check2(ROLL_RESULT, Dice_count, Rows) == 1:
                        break
            # Reset roll

    hit_rate = Hit / Sim_count * 100
    print("Completion rate to STEAL Kasugayama is: " + str(format(hit_rate, ".2f")), "%", sep="")

    """ *** Here be functions *** """

# Rolls a fresh set of dice
def roll(ROLL_RESULT, Dice_count):
    ROLL_RESULT.clear()
    for x in range(Dice_count[0]):
        ROLL_RESULT.append(random.randrange(1, 7, 1))

# Checks for double archer
def check1(ROLL_RESULT, Dice_count, Rows):
    roll_check = 0
    if Dice_count[0] >= 2:
        for x in ROLL_RESULT:
            if x == 4:
                roll_check += 1
                if roll_check >= 2:
                    Dice_count[0] = Dice_count[0] - 2
                    Rows[0] = 1
                    return 1
    else:
        return 0
    
# Checks for double knight
def check2(ROLL_RESULT, Dice_count, Rows):
    roll_check = 0
    if Dice_count[0] >= 2:
        for x in ROLL_RESULT:
            if x == 5:
                roll_check += 1
                if roll_check >= 2:
                    Dice_count[0] = Dice_count[0] - 2
                    Rows[1] = 1
                    return 1
    else:
        return 0
    
# Checks for Daimyo
def check3(ROLL_RESULT, Dice_count, Rows):
    if 6 in ROLL_RESULT:
        Dice_count[0] -= 1
        Rows[2] = 1
        return 1
    
def filterer(ROLL_RESULT, Dice_count, Rows):
    roll(ROLL_RESULT, Dice_count)
    if Rows[0] != 1:
        if check1(ROLL_RESULT, Dice_count, Rows) == 1:
            return 0
    if Rows[1] != 1:
        if check2(ROLL_RESULT, Dice_count, Rows) == 1:
            return 0
    if Rows[2] != 1:
        if check3(ROLL_RESULT, Dice_count, Rows) == 1:
            return 0
        else:
            Dice_count[0] = Dice_count[0] - 1
    else:
        Dice_count[0] = Dice_count[0] - 1

# Checks if there are enough dice left to continue
def dice_left(Rows, Dice_count):
    if Dice_count[0] < 2:
        return 0
    else:
        return 1

if __name__ == "__main__":
    main()