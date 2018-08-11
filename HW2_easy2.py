list = [1, 2, 2, 3, 4, 4, 5, 2, 5, 6, 7, 8]
list2 = [2, 4, 6, 6, 8]
i = 0
j = 0

while i < len(list2):
    while j < len(list):
        if list2[i] == list[j]:
            list.remove(list[j])
            print(list)
        else:
            j += 1
            print(list)
    else:
        i += 1



















#print(list)





