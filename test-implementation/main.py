#handles the general flow of the process
from loading import load_sheet
# from loading import load_students, load_periods
# from assignment import assign_students
# from macro import output_assignments

SPREADSHEET_ID = "1pt3gkk1QFjQ-6ZyiUoZmun-drKmmb_iL9w-vYkiIgQI"
SHEET_RANGE = "Sheet1!A1:E5"

if __name__ == "__main__":
    load_sheet(SPREADSHEET_ID, SHEET_RANGE)
    # students = load_students(SPREADSHEET_ID, SHEET_RANGE)
    # periods = load_periods(SPREADSHEET_ID, SHEET_RANGE)
    # assignments = assign_students(students, period_data)
    # output_assignments(assignments)
