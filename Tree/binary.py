class Node:
    def __init__(self, value = None) -> None:
        self.__value = value
        self.__left_node = None
        self.__right_node = None

    def add_to_left(self, left_node):
        self.__left_node = left_node
    
    def add_to_right(self, right_node):
        self.__right_node = right_node
    
    def set_value(self, value):
        self.__value = value

    def get_left(self ):
        return self.__left_node 
    
    def get_right(self):
        return self.__right_node
    
    def get_value(self):
        return self.__value
    
    def __str__(self) -> str:
        return self.__value

def insert(value, node):
    current_node_value = node.get_value()
    if current_node_value == None:
        node.set_value(value)
        return
    if current_node_value == value:
        return
    
    new_node = Node(value)
    if current_node_value < value:
        print("going right")
        right_node = node.get_right()
        if right_node == None:
            node.add_to_right(new_node)
        else:
            insert(value, node.get_right())
    else:
        print("going left")
        left_node = node.get_left()
        if left_node == None:
            node.add_to_left(new_node)
        else:
            insert(value, node.get_left())
    return


def inorder_traversal(node):
    if node != None:
        inorder_traversal(node.get_left())
        print(node.get_value())
        inorder_traversal(node.get_right())



if __name__ == "__main__":
    root_node = Node()
    insert(20, root_node)
    insert(10, root_node)
    insert(30, root_node)
    insert(40, root_node)
    insert(25, root_node)
    insert(15, root_node)
    insert(5, root_node)
    insert(45, root_node)
    insert(5, root_node)

    print()
    print()
    inorder_traversal(root_node)