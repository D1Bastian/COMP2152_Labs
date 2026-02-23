monday_class = {"Alice", "Bob", "Charlie", "David"}
wednesday_class = {"Eve", "Frank", "Grace", "Bob"}

monday_class.add("Hannah")

print(f"Monday class students: {monday_class}")
print(f"Wednesday class students: {wednesday_class}")
# both_days = monday_class.intersection(wednesday_class)
# print(f"Students attending both days: {both_days}")
print(f"Students attending both days: {monday_class & wednesday_class}")
print(f"All unique students attending either day: {monday_class | wednesday_class}")
print(f"Only Monday class students: {monday_class - wednesday_class}")
print(f"Only Wednesday class students: {wednesday_class - monday_class}")
print(f"Number of students attending Monday class: {len(monday_class)}")    
print(f"Number of students attending Wednesday class: {len(wednesday_class)}")
print(f"Only one class students: {monday_class ^ wednesday_class}")
all_students = monday_class.union(wednesday_class)
print(f"Total unique students attending classes: {len(all_students)}")
print(f"Is Monday Class a subset of All Students? {monday_class <= all_students} ")
print(f"Is Wednesday Class a subset of All Students? {wednesday_class <= all_students} ")    