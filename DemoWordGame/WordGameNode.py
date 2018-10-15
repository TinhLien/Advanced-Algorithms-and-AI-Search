#
#   Use this class definition to work from.
#   This way of reading the dictionary is quete messy.
#   It is done this way to make testing easier.
#
from Node import Node
from string import ascii_lowercase

valid_words = None


class WordGameNode(Node):
    def __init__(self, name, parent=None):
        # Ensure lowercase letters (no digits or special chars)
        for letter in name:
            assert letter in ascii_lowercase
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_children(self):
        child_words = []
        for idx, letter in enumerate(self.name):
            for char in ascii_lowercase:
                if char != self.name[idx]:
                    word = self.name[:idx] + char + self.name[idx + 1:]
                else:
                    continue
                if word in valid_words and not word in child_words:
                    child_words.append(WordGameNode(word, self))
        return child_words

    def get_path(self):
        if not self.get_parent():
            return [self]
        else:
            return [self] + self.get_parent().get_path()


def check_valid_words(word_to_check):
    global valid_words
    return word_to_check in valid_words


def read_dictionary(path, word_length):
    global valid_words
    if valid_words == None or len(valid_words[0]) != word_length:
        valid_words = []
        with open(path, "r") as file:
            for line in file.readlines():
                if len(line.strip()) == word_length:
                    valid_words.append(line.strip())
