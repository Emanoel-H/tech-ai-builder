students = {}

stop = "yes"

while stop == "yes":
    name = input("Enter your name: ")
    mean = float(input("Enter a mean number: "))
    students[name] = mean
    stop = input("Would you like to continue (yes/no): ")


for name in list(students.keys()):
    new_mean = students[name] + 1

    students[name] = students[name] = 10 if new_mean > 10 else new_mean

    if students[name] < 5:
        print(f"{name} is reproved for small mean")
        students.__delitem__(name)


for key, value in students.items():
    print(f"The student {key} has the mean {value}")

# print(students)