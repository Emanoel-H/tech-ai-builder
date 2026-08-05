means_list = []
stop = "yes"

while stop == "yes":
    value = float(input("Enter a mean number: "))
    means_list.append(value)
    stop = input("Would you like to continue (yes/no): ")

i = 0

while i < len(means_list):
    means_list[i] = means_list[i] + 1
    if means_list[i] > 10:
        means_list[i] = 10
    i = i + 1

for i in means_list:
    print(i)
