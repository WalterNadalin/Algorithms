from data_structures.adjacency_list import adjacency_list, color, queue

def breath_first_search(A, s):
  u = A.find(s)
  u[0].color = color.grey
  u[0].distance = 0

  Q = queue()
  Q.enqueue(s)

  while not Q.is_empty():
    u = Q.dequeue()
    l = A.find(u)

    for s in l[1:]:
      v = A.find(s)[0]

      if v.color is color.white:
        v.color = color.grey
        v.distance = l[0].distance + 1
        v.parent = l[0]
        Q.enqueue(v.key)

    l[0].color = color.black

def print_path(A, s, v):
  u = A.find(v)

  if v == s:
    print(s, end = ' ')
    return
  elif u[0].parent is None:
    print(f'No path from {s} to {v} exist')
    return
  else:
    print_path(A, s, u[0].parent.key)
    print(v, end = ' ')

if __name__ == "__main__":
  V = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'l']
  E = [('b', 'a'), ('c', 'a'), ('c', 'b'), ('d', 'b'), ('h', 'd'), ('b', 'h'), ('b', 'c'), ('e', 'c'), ('d', 'd'), ('f', 'd'), ('d', 'f'), ('g', 'e'), ('g', 'c')]
  A = adjacency_list(V, E)
  print('Adjacency list:')
  print(A)
  breath_first_search(A, 'a')
  print('\nPath from a to h:')
  print_path(A, 'a', 'h')
  print()
