# Will try myself from scratch
import json

class Node:
    def __init__(self) -> None:
        self.__is_end_of_word = False
        self.__next_nodes = {}
    
    def set_is_end_of_word(self, is_end_of_word):
        self.__is_end_of_word = is_end_of_word

    def get_is_end_of_word(self):
        return self.__is_end_of_word
    
    def set_next_node_if_exists(self, node, next_char):
        if next_char not in self.__next_nodes.keys():
            self.__next_nodes[next_char] = node
            # print(self)

    def get_next_node(self, char):
        return self.__next_nodes[char]

    def __str__(self) -> str:
        return json.dumps({
            "next": list(self.__next_nodes.keys()), 
            "end_of_word": self.__is_end_of_word
        })

def insert(node, word):
    for char in word:
        node.set_next_node_if_exists(Node(), char)
        node = node.get_next_node(char)
        print(node)
    node.set_is_end_of_word(True)
    print(node)

def search(node, word):
    for char in word:
        try:
            node = node.get_next_node(char)
            print(node)
        except KeyError:
            return [word, False]
    print(node)
    if not node.get_is_end_of_word():
        return [word, False]
    return [word, True]


if __name__ == "__main__":
    start_node = Node()
    insert(start_node, "start")
    print()
    insert(start_node, "stop")
    print()
    insert(start_node, "starting")

    print()
    print()
    print()
    print()

    print(search(start_node, "stop"), end="\n\n")
    print(search(start_node, "start"), end="\n\n")
    print(search(start_node, "starting"), end="\n\n")
    print(search(start_node, "stopping"), end="\n\n")
    print(search(start_node, "sit"), end="\n\n")
    print(search(start_node, "sitting"), end="\n\n")
    print(search(start_node, "apple"), end="\n\n")

    insert(start_node, "apple")
    print()
    print(search(start_node, "apple"), end="\n\n")
    print(search(start_node, "starting"), end="\n\n")
    print(search(start_node, "stopping"), end="\n\n")
    print(search(start_node, "sit"), end="\n\n")