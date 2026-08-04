means_list = [8.9, 7.5, 4.2, 1.4, 9.5]

i = 0
while i < 5:
    means_list[i] = means_list[i] + 1
    if means_list[i] > 10:
        means_list[i] = 10
    i = i + 1

for i in means_list:
    print(i)
