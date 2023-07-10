class Node:
    def __init__(self, data, next_node = None):
        self.data = data 
        self.next_node = next_node
        print(self.data)


class LinkedList: 
    def __init__(self, head = None):
        self.head = head
        # print(self)

    def append(self, node):
        # add element to the beginning of the list if the list is empty
        if self.head == None:
            self.head = None 
            return 
        # otherwise, traverse the list to find the last node 
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        # and add the node to the end 
        last_node.next_node = node
    

list = LinkedList()
list.append(Node("Bulldog"))
list.append(Node("Chihuahua"))
list.append(Node("German Shepard"))




# bulldog = Node("Bulldog")
# chihuahua = Node("Chihuahua")
# bulldog.next_node = chihuahua
# german_shepard = Node("German Shepard")
# chihuahua.next_node = german_shepard


