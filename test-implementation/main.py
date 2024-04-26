#handles the general flow of the process
from loading import load_sheet
# from loading import load_students, load_periods
from assignment import assign_students
# from macro import output_assignments

SPREADSHEET_ID = [
    "1Mn5APkaN1wZov8NB-fzREIPhW9JKVpttO47U-dG319k",
    "1Mn5APkaN1wZov8NB-fzREIPhW9JKVpttO47U-dG319k"
]
SHEET_RANGE = [
    "Sheet1!A2:E5",
    "Sheet2!A2:B9"
]

if __name__ == "__main__":
    student_data = load_sheet(SPREADSHEET_ID[0], SHEET_RANGE[0])
    # 'Name', 'Grade', 'Signed up?', 'Teacher1', 'Teacher2'
    period_data = load_sheet(SPREADSHEET_ID[1], SHEET_RANGE[1])
    # 'id', 'capacity'

    #students = [ ("sid", ["periodID",...]) ]
    students = []
    for row in student_data:
        if row[2]:#skip if already signed up
            continue

        # (sid, list of teachers)
        students.append(
            (row[0], row[3:])
        )
    #period_data = { "pid": int capacity_left, }
    periods={}
    for row in period_data:
        periods[row[0]]=row[1]

    period_assignments = assign_students(students, periods)
    #out data = { DICT
    #   "pid": [sid,sid,sid...],
    #}

    for pid in period_assignments.keys():
        print(f"Period ID [{pid}]: "+", ".join([s for s in period_assignments[pid]]))
