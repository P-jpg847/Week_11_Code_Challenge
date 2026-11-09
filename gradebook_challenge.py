# CIS 105 - Code Challenge: Grade Book
# Name: Precious Akinyele
# Section: 01
#
# Complete the five functions below where you see # TODO.
# Do not change the test code at the bottom of the file.
#
# The grade book is a dictionary:
#   keys   = student names (strings)
#   values = lists of test scores (numbers)
# Example: {"Alex": [90, 85, 95], "Jordan": [70, 80]}


def add_student(book, name): 
    """Add a new student with an empty score list.
    If the student is already in the book, print a message and change nothing."""
    # TODO
    if name in book:
        print("Student already in the book.")
    else:
        book[name] = []
    pass


def add_grade(book, name, grade):
    """Add a score to a student's list.
    If the student is not in the book yet, add the student first, then the score."""
    # TODO
     if name in book:
        book[name].append(grade)
    else:
        add_student(book, name)
        book[name].append(grade)
    pass


def student_average(book, name):
    """Return the average of a student's scores.
    Use .get() so this returns None instead of crashing
    if the student is not in the book."""
    # TODO
     grades = book.get(name)
    if grades is None:
        return None
    return sum(grades)/len(grades)
    pass


def top_student(book):
    """Return the name of the student with the highest average score."""
    # TODO
def top_student(book):
    top_student = None
    top_average = None
    for name in book:
        average = student_average(book, name)
        if average is not None and (top_average is None or average > top_average):
            top_student = name
            top_average = average
    return top_student
    pass


def print_report(book):
    """Print every student, their scores, and their average,
    one student per line. Loop over the dictionary with .items()."""
    # TODO
    def print_report(book):
        for name, score in book.items():
            print(name, score, student_average(book, name))
    pass


# ---------------- TEST CODE - DO NOT CHANGE BELOW THIS LINE ----------------

gradebook = {}

add_student(gradebook, "Alex")
add_student(gradebook, "Jordan")
add_student(gradebook, "Taylor")

add_grade(gradebook, "Alex", 90)
add_grade(gradebook, "Alex", 85)
add_grade(gradebook, "Alex", 95)

add_grade(gradebook, "Jordan", 70)
add_grade(gradebook, "Jordan", 80)

add_grade(gradebook, "Taylor", 100)
add_grade(gradebook, "Taylor", 95)
add_grade(gradebook, "Taylor", 90)
add_grade(gradebook, "Taylor", 85)

print_report(gradebook)
print("Top student:", top_student(gradebook))

# Expected output:
# Alex: [90, 85, 95] Average: 90.0
# Jordan: [70, 80] Average: 75.0
# Taylor: [100, 95, 90, 85] Average: 92.5
# Top student: Taylor
