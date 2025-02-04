#!/usr/bin/env python3

def join_lists(list1, list2):
    # join_lists will return a list that contains every value from both l1 and l2
    join = set(list1) | set(list2) 
    return list(join) 

def match_lists(list1, list2):
    # match_lists will return a list that contains all values found in both l1 and l2
    match = set(list1) & set(list2)
    return list(match) 
 
def diff_lists(list1, list2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    different = set(list1) ^ set(list2)
    return list(different)

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))