"""
Question 8: Example where Copilot's suggestion might introduce a subtle bug
Scenario: Sorting a list of dictionaries
"""

def sort_students_by_grade(students):
    """
    Sort students by grade in descending order.
    Copilot might suggest using sort() which modifies the original list.
    """
    # BUGGY VERSION: This modifies the original list in-place
    students.sort(key=lambda x: x['grade'], reverse=True)
    return students


# Test the buggy version
students_list = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

print("Original list before sorting:")
print(students_list)

sorted_students = sort_students_by_grade(students_list)

print("\nSorted list:")
print(sorted_students)

print("\nOriginal list after sorting (UNEXPECTED BUG - list was modified!):")
print(students_list)
print("\nBUG: The original list was modified! This is a side effect.")
