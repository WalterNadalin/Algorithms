class colored:
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'

class color:
  white = 0
  grey = 1
  black = 2
  green = 3
  blue = 4

class empty_queue:
  def __init__(self):
    self.Q = []

  def enqueue(self, x):
    self.Q += [x]

  def dequeue(self):
    return self.Q.pop(-1)

  def is_empty(self):
    return not self.Q

  def __str__(self):
    return f'{self.Q!r}'

class adjacent_list:
  def __init__(self, V, E):
    self.list = [[node(v)] for v in V]

    for e in E:
      x = self.find(e[1])
      x += [e[0]]

  def __str__(self):
    s = ''

    for x in self.list:
      s += str(x[0])

      for v in x[1:]:
        s += ' \u2192 ' + str(v)

      s += '\n'

    return s[:-1]

  def __getitem__(self, i):
    return self.list[i]

  def find(self, v):
    i = 0

    while self.list[i][0] != node(v):
      i += 1

    return self[i]

class node:
  def __init__(self, v):
    self.key = v
    self.cc = None
    self.d = None
    self.f = None
    self.color = color.white
    self.distance = None
    self.parent = None
    self.count = 0

  def __repr__(self):
    s = str(self.key)

    if self.color is color.white:
      return s
    elif self.color is color.grey or self.color is color.blue:
      return f'{colored.red}' + s + f'{colored.end}'
    else:
      return f'{colored.green}' + s + f'{colored.end}'

  def __eq__(self, other):
    return self.key == other.key

if __name__ == "__main__":
  V = ['a', 'b', 'c', 'd']
  E = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'd'), ('d', 'b')]
  example = adjacent_list(V, E)
  print(example)
