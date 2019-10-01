class nodeType:

    def __init__(self, info):
        self.info = info
        self.link = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def buildList(self, new_node):

        currNode = self.head

        if currNode is None:
            self.head = new_node
            self.size += 1
            return

        else:
            while currNode.link is not None and currNode.link.info <= new_node.info:
                currNode = currNode.link
                if currNode.link.info >= new_node.info:
                    tempNode = currNode.link
                    currNode.link = new_node
                    new_node.link = tempNode

        currNode.link = new_node
        self.size += 1

    def traverse(self):
        currNode = self.head

        if currNode is None:
            print("Nothing in LinkedList")
        else:
            while currNode is not None:
                print("Current address:", hex(id(currNode)), "Info:", currNode.info,
                      "Link:", hex(id(currNode.link)))
                currNode = currNode.link