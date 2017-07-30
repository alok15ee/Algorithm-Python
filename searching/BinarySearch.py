#!/usr/bin/python

'''

Binary Search is an algorithm which helps to simplifies the search of an element using the Divide and Conquer Strategy.

EX: When a user logs-in into facebook, it needs to search for the username in the database:

Binary search is an algorithm which only works when the list(to search for) is in sorted order.

Running time :

O(logn)
'''




def binary_search(search_list, item):

    low = search_list[0]
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high)/2
        search_item = search_list[mid]
        if item == search_item:
            print "Required item is at " + str(mid) + "th index"
            return mid
        else:
            if item > search_item:
                low = mid + 1
            elif item <= search_item:
                high = mid -1


search_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
binary_search(search_list, 32)

