#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    list1 = []
    list2 = []
    list1.append(1)
    list2.append(list1)
    for i in range(n - 1):
        list1 = []
        tmplist = list2[-1]
        i = 0
        while i < len(tmplist):
            if i != 0:
                list1.append(tmplist[i] + tmplist[i - 1])
            else:
                list1.append(1)
            i += 1
        list1.append(1)
        list2.append(list1)
    return list2
