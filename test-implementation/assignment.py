import random as rd
from std import *
#handles actually assigning students to their classes for flex

#takes in students, period capacities
#outputs where each student goes

#students = [ LIST
#    ("sid", ["periodID1",...])
#]
#period_data = { DICT
#    "pid": int capacity_left,
#}

#out data = { DICT
#   "pid": [sid,sid,sid...],
#}
def assign_students(students, period_data):
    out_data = {}
    for c in period_data.keys():
        out_data[c] = []

    rd.shuffle(students)  # Randomize the order of students

    for stud in students:
        rd.shuffle(stud[1]) #shuffle unwanted classees
        classes = stud[1]
        '''STILL NEEDS TO SORT BASED ON CAPACITY'''
        for c in classes:
            '''GIVES ERROR IF PERIOD_DATA[c] DOES NOT EXIST'''
            capacity = int(period_data[c])
            if capacity>0:
                out_data[c].append(stud[0])
                capacity-=1
                period_data[c] = str(capacity)
                break
        #need to recursively assign students who didn't get their preferenced ces if not enough space in all 7 of a student's ces.

    return out_data