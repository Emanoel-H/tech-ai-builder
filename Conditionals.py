age = input("How old are you?")

if age.strip().isnumeric():
    answer = "You can drive" if int(age) >= 18 else "You can't drive"
    print(answer)
else:
    print("Age must be a numeric value")