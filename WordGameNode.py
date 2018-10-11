#
#   Use this class definition to work from.
#   This way of reading the dictionary is quete messy.
#   It is done this way to make testing easier.
#
from Node import Node
from string import ascii_lowercase
from read_dictionary import read_dictionary

valid_words = None

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase

      global valid_words
      if valid_words == None or len(valid_words) != len(name):
         # We only need to examine words which have the same length as our word (self.name)
         valid_words = read_dictionary("/etc/dictionaries-common/words", len(name))
      self.name = name
      self.parent = parent

   def __str__(self):
      return self.name

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
