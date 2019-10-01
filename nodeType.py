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

        else:
            if self.head.info > new_node.info:
                new_node.link = self.head
                self.head = new_node
                self.size += 1
                return
            else:
                while currNode is not None:
                    if currNode.link is None:
                        currNode.link = new_node
                        self.size += 1
                        return

                    else:
                        if currNode.link.info > new_node.info:
                            temp_link = currNode.link
                            currNode.link = new_node
                            new_node.link = temp_link
                            print("temp_link:", temp_link.info, "| currNode:",
                                  currNode.info, "| new_node:", new_node.info)
                            self.size += 1
                            return

                    currNode = currNode.link


    def traverse(self):
        currNode = self.head

        if currNode is None:
            print("Nothing in LinkedList")
        else:
            while currNode is not None:
                print("Current address:", hex(id(currNode)), "Info:", currNode.info,
                      "Link:", hex(id(currNode.link)))
                currNode = currNode.link