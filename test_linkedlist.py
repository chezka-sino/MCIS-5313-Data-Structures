from nodeType import *

def unsorted_linkedlist(list_num):
    new_linkedlist = LinkedList()

    for item in list_num:
        new_node = nodeType(item)
        new_linkedlist.buildList(new_node)

    return new_linkedlist

def sorted_linkedlist(list_num):
    new_linkedlist = LinkedList()

    for item in list_num:
        new_node = nodeType(item)
        new_linkedlist.buildList_sorted(new_node)

    return new_linkedlist

if __name__ == "__main__":

    list_num = [17, 19, 63, 44]

    unsorted = unsorted_linkedlist(list_num)
    sorted = sorted_linkedlist(list_num)

    print("UNSORTED LINKED LIST SAMPLE")
    print("LinkedList Size:", unsorted.size)
    unsorted.traverse()
    print()

    print("SORTED LINKED LIST SAMPLE")
    print("LinkedList Size:", unsorted.size)
    sorted.traverse()