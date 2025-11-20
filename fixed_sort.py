"""
Question 8: Corrected version - avoiding the subtle bug
"""

def sort_students_by_grade_fixed(students):
    """
    Sort students by grade in descending order WITHOUT modifying original list.
    
    CORRECTION: Use sorted() instead of sort() to avoid modifying the original list.
    - sort() modifies the list in-place (side effect)
    - sorted() returns a new sorted list (no side effect)
    """
    # FIXED VERSION: Returns a new sorted list, original unchanged
    return sorted(students, key=lambda x: x['grade'], reverse=True)


# Test the fixed version
students_list = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

print("Original list before sorting:")
print(students_list)

sorted_students = sort_students_by_grade_fixed(students_list)

print("\nSorted list:")
print(sorted_students)

print("\nOriginal list after sorting (FIXED - list unchanged!):")
print(students_list)
print("\nSUCCESS: The original list remains unchanged!")

"""
JUSTIFICATION:
- Using sort() creates a side effect by modifying the input list
- This can cause bugs when the caller expects the original list to remain unchanged
- sorted() creates a new list, following functional programming principles
- This makes the function more predictable and easier to test
"""
