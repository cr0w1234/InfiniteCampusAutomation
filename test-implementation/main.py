#handles the general flow of the process
from loading import load_sheet
# from loading import load_students, load_periods
# from assignment import assign_students
# from macro import output_assignments

SPREADSHEET_ID = [
    "1pt3gkk1QFjQ-6ZyiUoZmun-drKmmb_iL9w-vYkiIgQI",
    "1pt3gkk1QFjQ-6ZyiUoZmun-drKmmb_iL9w-vYkiIgQI"
]
SHEET_RANGE = [
    "Sheet1!A1:E5",
    "Sheet1!A1:E5"
]

if __name__ == "__main__":
    student_data = load_sheet(SPREADSHEET_ID[0], SHEET_RANGE[0])
    # 'Name', 'Grade', 'Signed up?', 'Teacher1', 'Teacher2'
    period_data = load_sheet(SPREADSHEET_ID[1], SHEET_RANGE[1])
    # 'id', 'capacity'

    #students = [ ("sid","pref1ID","pref2ID",["other_periodID",...]) ]
    students = []
    for row in student_data:
        if row[2]:#skip if already signed up
            continue

        students.append(
            (row[0], row[3], row[4], ["oh no, where's the data?"])
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
