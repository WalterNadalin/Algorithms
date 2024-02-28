from copy import copy
from collections import OrderedDict

class empty_node:
    def __init__(self):
        self.start = None
        self.depth = None
        self.parent = None
        self.child = OrderedDict()
        self.slink = None
        self.count = 0
        self.length = 0

    def __str__(self):
        return f'[{self.start}, {self.depth}], {self.count} ↴'
        # return f'[{self.start + self.parent.depth}, {self.start + self.depth}] ↴'

class empty_leaf:
    def __init__(self):
        self.start = None
        self.depth = None
        self.parent = None
        self.child = OrderedDict()
        self.slink = None
        self.count = None
        self.length = 0

    def __str__(self):
        return f'[{self.start}, {self.depth}] → ({self.start}) {text[self.start: self.start + self.depth + 1]}' 
        #return f'[{self.start + self.parent.depth + 1}, {self.start + self.depth + 1}] → ({self.start + 1}) , {text[self.start: len(text)]}'

def split_edge(node, depth, text):
    split = empty_node()
    split.start = node.start
    split.depth = depth
    node.parent.child[text[node.start + node.parent.depth]] = split
    split.parent = node.parent
    split.child[text[node.start + depth]] = node
    node.parent = split

    return split

def create_leaf(position, node, depth, text):
    leaf = empty_leaf()
    leaf.start, leaf.depth = position, len(text) - position - 1
    node.child[text[position + depth]] = leaf
    leaf.parent = node
    return leaf

def bf_construction(text):
    root = empty_node()
    root.depth = 0
    node, depth = root, 0
    root.count = 0

    for i in range(len(text)):
        while depth == node.depth and node.child.get(text[i + depth], None) is not None:
            node = node.child.get(text[i + depth], None)
            depth += 1

            while depth < node.depth and text[node.start + depth] == text[i + depth]:
                depth += 1

        if depth < node.depth:
            node = split_edge(node, depth, text)

        node = create_leaf(i, node, depth, text)
        node, depth = root, 0

    return root

def visualize(node, level = 0):
    if node == None:
        return

    for key, value in sorted(node.child.items()):
        print('\t' * level, key, ': ', value, sep = '')
        visualize(value, level + 1)

def suffix_link(node, depth, text):
  slink = node.parent.slink

  while slink.depth < depth - 1:
    slink = slink.child.get(text[node.start + slink.depth + 1], None)

  return slink

def compute_suffix_link(node, text):
  slink = suffix_link(node, node.depth, text)

  if slink.depth > node.depth - 1:
    slink = split_edge(slink, node.depth - 1, text)

  node.slink = slink

def mccreight(text):
    root = empty_node()
    root.depth = 0
    root.slink = root
    node, depth = root, 0
    root.count = 0

    for i in range(len(text)):
        while depth == node.depth and node.child.get(text[i + depth], None) is not None:
            node = node.child.get(text[i + depth], None)
            depth += 1

            while depth < node.depth and text[node.start + depth] == text[i + depth]:
                depth += 1

        if depth < node.depth:
            node = split_edge(node, depth, text)

        leaf = create_leaf(i, node, depth, text)

        if node.slink is None:
          compute_suffix_link(node, text)

        node, depth = node.slink, 0 if depth < 1 else depth - 1

    return root

def is_empty(pattern):
  return not pattern

def traverse(node):
  shifts = []

  if is_empty(node.child):
    return [node.start]

  for value in node.child.values():
    shifts += traverse(value)

  return shifts

def search(pattern, root, text):
  pattern = [character for character in pattern]
  depth = 0
  node = root

  while not is_empty(pattern):

    if depth > node.depth - 1:
      node = node.child.get(pattern[0], None)

      if node is None:
        break

    if pattern[0] == text[node.start + depth]:
      pattern.pop(0)
    else:
      break

    depth += 1

  if is_empty(pattern):
    return traverse(node)
  else:
    return 'The pattern does not appear anywhere in the text.'

if __name__ == '__main__':
  text = "abcdefghilmnopqrstuvz$"
  text = "mississippi$"
  print('Brutal construction')
  root = bf_construction(text)
  visualize(root)

  print('\nMcCreight`s algorithm')
  root = mccreight(text)
  visualize(root)


  
