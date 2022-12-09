# Task 1.

def task1(list1, list2):
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    return list3

# Task 2.

def task2(array):
    for i in array:
        if i == 0:
            array.remove(i)
    return array

