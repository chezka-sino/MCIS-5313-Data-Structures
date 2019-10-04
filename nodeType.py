class nodeType:

    def __init__(self, info):
        self.info = info
        self.link = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def buildList(self, new_node):
        # Inserts new node at the end of the linkedlist
        currNode = self.head

        if currNode is None:
            self.head = new_node
            self.size += 1

        else:
            while currNode is not None:
                tempNode = currNode
                currNode = currNode.link

            tempNode.link = new_node
            self.size += 1

    def buildList_sorted(self, new_node):
        # Inserts new node in a sorted way

        currNode = self.head

        if currNode is None:
            #sets the newnode as the head if linkedlist is empty
            self.head = new_node
            self.size += 1

        else:
            # sets new node as the head if smaller than current head
            if self.head.info > new_node.info:
                new_node.link = self.head
                self.head = new_node
                self.size += 1
            else:
                # traverses to through the linkedlist and inserts the new
                # node accordingly
                while currNode is not None:
                    # inserts at the end of the list
                    if currNode.link is None:
                        currNode.link = new_node
                        self.size += 1
                        return

                    else:
                        # compares info of current node to new node and inserts
                        # new node if applicable
                        # exits function if node is inserted successfully
                        if currNode.link.info > new_node.info:
                            temp_link = currNode.link
                            currNode.link = new_node
                            new_node.link = temp_link
                            self.size += 1
                            return

                    # moves current node to the next on the linkedlist if new node
                    # is not inserted yet
                    currNode = currNode.link


    def traverse(self):
        # traverses through the linked list
        currNode = self.head

        if currNode is None:
            print("Nothing in LinkedList")
        else:
            while currNode is not None:
                print("Current address:", hex(id(currNode)), "Info:", currNode.info,
                      "Link:", hex(id(currNode.link)))
                currNode = currNode.link