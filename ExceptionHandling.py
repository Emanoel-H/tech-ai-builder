try:
    age = int(input("How old are you? "))
except ValueError:
    print("Oops! That isn't an integer!")