from nodeType import *

if __name__ == "__main__":

    new_linkedlist = LinkedList()
    list_num = [17, 19, 63, 44]

    for item in list_num:
        new_node = nodeType(item)
        new_linkedlist.buildList(new_node)

    new_linkedlist.traverse()