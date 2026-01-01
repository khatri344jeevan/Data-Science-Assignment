# Build a simple grade calculator fot the multiple students. Input their marks in a list and print the grade using a function.
def grading(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks_list = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks_list.append(mark)

print("Grade Report")

for i in range(n):
    grade = grading(marks_list[i])
    print(f"Student {i+1}: Marks = {marks_list[i]}, Grade = {grade}")