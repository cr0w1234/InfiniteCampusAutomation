import random as rd
from std import *
#handles actually assigning students to their classes for flex

#takes in students, period capacities
#outputs where each student goes

#students = [ LIST
#    ("sid","pref1ID","pref2ID",["other_periodID",...])
#]
#period_data = { DICT
#    "pid": int capacity_left,
#}

#out data = { DICT
#   "pid": [sid,sid,sid...],
#}
def assign_students(students, period_data):
    out_data = {}
    for class in period_data.keys():
        out_data[class] = []

    rd.shuffle(students)  # Randomize the order of students

    for stud in students:
        rd.shuffle(stud[4])#shuffle unwanted classes
        classes = [stud[2],stud[3]] + stud[4] # and then create assignment priorities
        for class in classes:
            if period_data[class]>0:
                out_data[class].append(stud)
                period_data[class]-=1
                break
        #need to recursively assign students who didn't get their preferenced classes if not enough space in all 7 of a student's classes.

    return out_data
