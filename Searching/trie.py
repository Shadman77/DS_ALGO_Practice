class node:
    def __init__(self, char, end_of_a_word, next_chars_mapping = {}):
        self.__char = char
        self.__end_of_a_word = end_of_a_word
        self.__next_chars_mapping = next_chars_mapping
    
    def get_next(self, char):
        return self.__next_chars_mapping[char]
    
    def insert(self, char, node):
        self.__next_chars_mapping[char] = node

if __name__ == "__main__":
     start = {}
     