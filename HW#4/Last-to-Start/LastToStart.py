# Author: Michael Smith
# Date: February, 2021
# Description: Program reads the act.txt input file that 
# contains the activities data. Performs Last-to-Start 
# selection based upon the start and finish time of each 
# activity to order them. Outputs the results to the terminal. 
# The resources I used were mainly Piazza, other classmates, 
# and the lectures.

# This function sorts activities by start times then implements 
# the Last-to-Start selection method and returns activity 
# that was selected.  Variable is the activity set array. I
# had written good pseudocode for this function so I only
# used piazza/lectures for help on section.
def lastToStart(acts):
    actSelected = []
    acts = sorted(acts, key=lambda k: k['start'])
    actTime = max([x['last'] for x in acts])

    while acts:
        act = acts.pop()
        if act['last'] <= actTime:
            actSelected.append({
                'idx': act['idx'],
                'start': act['start']
            })
            actTime = act['start']

    return actSelected

# This reads the data from the act.txt file which contains
# activity groups/sets. Prints the results to the terminal. 
# I had trouble on how to properly read the act.txt file and
# got a lot of advice from another student in the class. We 
# mainly worked on the while loop together.
with open("act.txt", "r") as inputFile:
    lines = inputFile.read().splitlines()
    sets = []
    acts = []
    i = 1

    while lines:
        line = lines.pop(0)
        line = [int(num) for num in line.split(" ")]
        if len(line) == 1 or not lines:
            if len(acts):
                sets.append(acts)
                acts = []
        else:
            acts.append({
                'idx': line[0],
                'start': line[1],
                'last': line[2]
            })
            
    print("Last-to-Start Results:")
    print("")
    for st in sets:
        print("Set " + str(i))
        selected = lastToStart(st)
        selected = sorted(selected, key=lambda k: k['start'], reverse=False)
        print("Number of activities selected = " + str(len(selected)))
        print("Activities: " + (" ".join([str(x['idx']) for x in selected])))
        print("")
        i = i + 1
