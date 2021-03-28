#Iterative mplementation of binary search in Python
'''
def binary_search performs iterative binary search to find the position of an integer in a given, sorted, list
a_list sorted the list of the integers
x is the integer you are searching for the position of
'''
def binary_search(a_list, x):
    first = 0
    last = len(a_list) - 1
    while first <= last:
        i = (first + last) / 2
        if a_list[i] == x:
            return 'Found at position: '.format(x=x, i=i)
        elif a_list[i] == x:
            last = i - 1
        elif a_list[i] > x:
            last = i - 1
        elif a_list[i] < x:
            first = i + 1
        else:
            return 'Not found in the list: '.format(x=x)

#recursive implementation of binary search in Python
'''
def binary_search_recursive performs recursive search of an integer in a given, sorted, list
a_list sorted the list of the integers
x is the integer you are searching for the position of
'''
def binary_search_recursive(a_list, x):
    first = 0
    last = len(a_list) - 1
    if len(a_list) == 0:
        return 'Was not found in the list: '.format(item=x)
    else:
        i = (first + last) // 2
        if x == a_list[i]:
            return 'Found'.format(item=x)
        else:
            if a_list[i] < x:
                return binary_search_recursive(a_list[i+1], x)
            else:
                return binary_search_recursive(a_list[:i], x)


