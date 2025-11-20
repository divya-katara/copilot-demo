"""
Example with repetitive code that needs refactoring
"""

def process_student_data():
    """Process student data with repetitive code."""
    # Student 1
    name1 = "Alice"
    age1 = 20
    grade1 = 85
    print(f"Student: {name1}")
    print(f"Age: {age1}")
    print(f"Grade: {grade1}")
    print(f"Status: {'Pass' if grade1 >= 50 else 'Fail'}")
    print("-" * 30)
    
    # Student 2
    name2 = "Bob"
    age2 = 21
    grade2 = 92
    print(f"Student: {name2}")
    print(f"Age: {age2}")
    print(f"Grade: {grade2}")
    print(f"Status: {'Pass' if grade2 >= 50 else 'Fail'}")
    print("-" * 30)
    
    # Student 3
    name3 = "Charlie"
    age3 = 19
    grade3 = 78
    print(f"Student: {name3}")
    print(f"Age: {age3}")
    print(f"Grade: {grade3}")
    print(f"Status: {'Pass' if grade3 >= 50 else 'Fail'}")
    print("-" * 30)

if __name__ == "__main__":
    process_student_data()
