class colored:
    red = '\033[91m'
    end = '\033[0m'

class color:
  black = 0
  red = 1

class side:
  right = 0
  left = 1

def reverse_side(x):
    return side.left if x is side.right else side.right

class rbtree:
  def __init__(self, *args):
    elements = [args]
    self._root = node(args[0])

    for x in args[1:]:
      self.insert(x)

  def __str__(self, x = None, l = 0):
      x = self.root if x is None else x
      s = '' if x.right is None else self.__str__(x.right, l + 1)
      s += '\t' * l + str(x) + '\n'
      s += '' if x.left is None else self.__str__(x.left, l + 1)
      return s

  @property
  def root(self):
      return self._root

  @root.setter
  def root(self, x):
      self._root = x

      if x is not None:
        x.parent = None
        x.color = color.black

  def minimum(self):
    return self.root.minimum()

  def maximum(self):
    return self.root.maximum()


  def search(self, v):
    return self.root.search(v)

  def insert_bst(self, v):
    x = self.root

    while x.key != v:
      if x.key < v:
        if x.right is None:
          x.set_child(side.right, node(v))
          return x.right

        x = x.right
      else:
        if x.left is None:
          x.set_child(side.left, node(v))
          return x.left

        x = x.left

    return

  def insert(self, v):
    x = self.insert_bst(v)

    if x is None:
      return

    x.color = color.red
    self.fix_insert(x)

  def fix_insert(self, x):
    while not x.is_root() and (not x.parent.is_root() and x.parent.color is color.red):
      if self.color(x.uncle()) is color.red:
        x = self.fix_insert_one(x)
      else:
        if x.childhood_side() is not x.parent.childhood_side():
          x = self.fix_insert_two(x)

        self.fix_insert_three(x)

    self.root.color = color.black

  def fix_insert_one(self, x):
    x.parent.color = color.black
    x.uncle().color = color.black
    x.grandparent().color = color.red
    return x.grandparent()

  def fix_insert_two(self, x):
    parent = x.parent
    self.rotate(parent, reverse_side(x.childhood_side()))
    return parent

  def fix_insert_three(self, x):
    grandparent = x.grandparent()
    x.parent.color = color.black
    x.grandparent().color = color.red
    self.rotate(grandparent, reverse_side(x.childhood_side()))

  def remove(self, v):
    x = self.search(v)

    if x is None:
      return
    elif x.left is None:
        self.transplant(x, x.right)
        return x
    elif x.right is None:
        self.transplant(x, x.left)
        return x

    y = x.right.minimum()
    v = y.key
    y = self.remove(v)
    x.key = v
    return y

  def transplant(self, x, y):
    if x.is_root():
      self.root = y
    else:
      s = x.childhood_side()
      x.parent.set_child(s, y)

  def color(self, x):
    if x is None:
      return color.black

    return x.color

  def rotate(self, x, s):
    rs = reverse_side(s)

    y = x.get_child(rs)
    self.transplant(x, y)
    beta = y.get_child(s)

    if beta is None:
      y.set_child(s, x)
    else:
      self.transplant(beta, x)

    x.set_child(rs, beta)

class node:
  def __init__(self, v):
    self.left = None
    self.right = None
    self.key = v
    self.parent = None
    self.color = color.black

  def __str__(self):
    s = f'[{self.key}]'
    return f'{colored.red}' + s + f'{colored.end}' if self.color is color.red else s

  def __repr__(self):
    s = f'{self.__class__.__name__}({self.key})'
    return f'{colored.red}' + s + f'{colored.end}' if self.color is color.red else s

  def is_root(self):
    return self.parent is None

  def is_right_child(self):
    return not self.is_root() and self.parent.right is self

  def sibling(self):
    return self.parent.left if self.is_right_child() else self.parent.right

  def childhood_side(self):
    return side.right if self.is_right_child() else side.left

  def get_child(self, s):
    return self.right if s is side.right else self.left

  def set_child(self, s, x):
    if s is side.right:
      self.right = x
    else:
      self.left = x

    if x is not None:
      x.parent = self

  def uncle(self):
    return self.parent if self.parent is None else self.parent.sibling()

  def grandparent(self):
    parent = self.parent
    return parent if parent is None else parent.parent

  def minimum(self):
    x = self

    while x.left is not None:
      x = x.left

    return x

  def maximum(self):
    x = self

    while x.right is not None:
      x = x.right

    return x

  def successor(self):
    if self.right is None:
      x = self
      y = x.parent

      while y is not None and x.is_right_child():
        x = y
        y = x.parent

      return y

    return self.right.minimum()

  def search(self, v):
    x = self

    while x is not None:
      if x.key == v:
        return x
      elif x.key < v:
        x = x.right
      else:
        x = x.left

if __name__ == "__main__":
  example = rbtree(4, 7, 12, 10, 13, 3, 15, 16)
  print(example)
  #print(example.maximum())
  #print(example.minimum())
  #example.insert(3)
  #print(example)
  #print(example.search(3))
  x = example.minimum()

  while x is not example.maximum():
    print(x, end = ' ')
    x = x.successor()

  print(x)


