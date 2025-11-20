"""
Refactored version using Copilot suggestions
"""

class Student:
    """Student class to encapsulate student data."""
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_status(self):
        """Determine if student passed or failed."""
        return 'Pass' if self.grade >= 50 else 'Fail'
    
    def display_info(self):
        """Display student information."""
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Status: {self.get_status()}")
        print("-" * 30)


def process_student_data_refactored():
    """Process student data using refactored class-based approach."""
    students = [
        Student("Alice", 20, 85),
        Student("Bob", 21, 92),
        Student("Charlie", 19, 78)
    ]
    
    for student in students:
        student.display_info()


if __name__ == "__main__":
    process_student_data_refactored()
