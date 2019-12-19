#!/usr/bin/python3
def weight_average(my_list=[]):
    newlist = my_list.copy()
    newlist2 = []
    mullist = my_list.copy()
    if my_list:
        for i in range(len(newlist)):
            for j in range(len(newlist[i])):
                if j == 1:
                    newlist2.append(newlist[i][j])
                else:
                    mullist[i] = newlist[i][j] * newlist[i][j + 1]
        return(sum(mullist) / sum(newlist2))
    else:
        return(0)
