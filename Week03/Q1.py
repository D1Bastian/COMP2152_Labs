grades = [85, 92, 78, 95, 88]
# print(grades)
grades.append(90)
# print(grades)
grades.sort()
# print(grades)
average = sum(grades) / len(grades)
# print("The average grade is: {:.2f}".format(average))
print(f"The average grade is: {average:.2f}")
print(f"highest grade: {grades[-1]}")
print(f"lowest grade: {grades[0]}")
print(f"number of grades: {len(grades)}")
print(f"sorted grades: {grades}")


