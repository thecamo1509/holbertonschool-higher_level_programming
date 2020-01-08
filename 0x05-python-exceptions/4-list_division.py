#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            newlist.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            newlist.append(0)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0)
        finally:
            pass
    return(newlist)
