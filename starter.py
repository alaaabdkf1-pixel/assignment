"""
Python Fundamentals Quiz
Student Starter Template

Instructions:
- Complete each function.
- Do NOT use for or while loops.
"""

def student_info(name, age):
    """Return a formatted sentence with the student's name and age."""
    return f"name:{name},age:{age}"


def swap(a, b):
    """Return the two values in reverse order."""
    return b,a
    


def first_and_last(items):
    """Return the first and last element of the list."""
    return items[0]+items[-1]
    


def get_grade(student, grades):
    """Return the student's grade or 'Student not found'."""
    return grades.get(student, "student not found")
 
    


def remove_duplicates(numbers):
    """Return a set containing the unique values."""
    return set(numbers)



if __name__ == "__main__":
    print("Run your own tests here.")
