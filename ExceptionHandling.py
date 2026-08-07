try:
    age = int(input("How old are you? "))

    people = 3

    people_2 = "John, Mary and Joseph"

    people + people_2
except ValueError:
    print("Oops! That isn't an integer!")
except TypeError:
    print("Oops! you cannot sum a number with a string!")