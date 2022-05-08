class SinglyNode:
    def __init__(self, value, next_node_addr=None):
        self.__value = value
        self.__next_node_addr = next_node_addr

    def set_value(self, value):
        self.__value = value
        return True

    def get_value(self):
        return self.__value

    def set_next_node_addr(self, next_node_addr):
        self.__next_node_addr = next_node_addr
        return True

    def get_next_node_addr(self):
        return self.__next_node_addr


def traverse(header):
    print(header.get_value())
    if header.get_next_node_addr() == None:
        print()
    else:
        traverse(header.get_next_node_addr())


def add(header, value):
    if header.get_value() == None:
        header.set_value(value)
    elif header.get_next_node_addr() == None:
        new_node = SinglyNode(value)
        header.set_next_node_addr(new_node)
    else:
        add(header.get_next_node_addr(), value)


def delete_last(header):
    next_node = header.get_next_node_addr()
    if next_node == None:
        header.set_value(None)
    elif next_node.get_next_node_addr() == None:
        header.set_next_node_addr(None)
    else:
        delete_last(next_node)


def delete_nth(header, n, i=1):
    next_node = header.get_next_node_addr()
    if n == 1:
        header.set_value(next_node.get_value())
        header.set_next_node_addr(next_node.get_next_node_addr())
    elif next_node == None:
        header.set_value(None)
    elif i == n-1:
        header.set_next_node_addr(next_node.get_next_node_addr())
    elif next_node.get_next_node_addr() == None:
        header.set_next_node_addr(None)
    else:
        delete_nth(next_node, n, i + 1)

def add_nth(node, value, n, i = 1, prev_node = None):
    if n == i:
        if prev_node == None:
            new_node = SinglyNode(value=node.get_value(), next_node_addr=node.get_next_node_addr())
            node.set_value(value)
            node.set_next_node_addr(new_node)
        else:
            new_node = SinglyNode(value=value, next_node_addr=node)
            prev_node.set_next_node_addr(new_node)
    else:
        add_nth(node.get_next_node_addr(), value, i+1, node)



if __name__ == "__main__":
    header = SinglyNode(1)
    add(header, 2)
    add(header, 3)
    add(header, 4)
    add(header, 5)
    traverse(header)


    delete_last(header)
    delete_last(header)
    delete_last(header)
    delete_last(header)
    delete_last(header)
    traverse(header)
    
    add(header, 5)
    for i in range(1, 5):
        add(header, i)
    traverse(header)
    
    delete_nth(header, 2)
    traverse(header)
    
    delete_nth(header, 1)
    delete_nth(header, 1)
    delete_nth(header, 1)
    delete_nth(header, 1)
    traverse(header)
    
    add_nth(header, 1, 1)
    traverse(header)
    
    # print(header.get_value())
