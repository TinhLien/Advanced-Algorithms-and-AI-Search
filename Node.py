class Node:
   def __init__(self, name, children):
      self.name = name
      self.children = children

   def __str__(self):
      return self.name
      #return "N({0}, {1})".format(self.name, self.children)

   def __repr__(self):
      return str(self)

   def get_children(self):
      return self.children

   # See https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes

   def __eq__(self, other):
      """Override the default Equals behavior"""
      if isinstance(other, self.__class__):
         return self.name == other.name
      return NotImplemented

   def __ne__(self, other):
      """Define a non-equality test"""
      if isinstance(other, self.__class__):
         return not self.__eq__(other)
      return NotImplemented

   def __hash__(self):
      """Override the default hash behavior (that returns the id or the object)"""
      return hash(tuple(sorted(self.__dict__.items())))