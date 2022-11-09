class node:
    def __init__(self, char, end_of_a_word, next_chars_mapping = {}):
        self.__char = char
        self.__end_of_a_word = end_of_a_word
        self.__next_chars_mapping = next_chars_mapping
    
    def get_next(self, char):
        if char in self.__next_chars_mapping.keys():
            return self.__next_chars_mapping[char]
        else:
            return None
    
    def insert(self, char, node):
        self.__next_chars_mapping[char] = node

    def check_if_end_of_word(self):
        return self.__end_of_a_word

if __name__ == "__main__":
     start = {}

     new_word = "start"
     for i in range(len(new_word)-1):
        if new_word[i] in start.keys():
            node = start.keys
     