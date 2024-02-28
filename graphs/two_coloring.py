from adjacent_list import adjacent_list, color, empty_queue

def breath_first_search(A, s):
  u = A.find(s)
  u[0].color = color.green
  u[0].distance = 0

  Q = empty_queue()
  Q.enqueue(s)

  while not Q.is_empty():
    u = Q.dequeue()
    l = A.find(u)

    for s in l[1:]:
      v = A.find(s)[0]
      distance = l[0].distance + 1
      #print(l[0], v, distance)
      if v.color is color.white:
        v.distance = distance
        assign_color(v)
        v.parent = l[0]
        Q.enqueue(v.key)
      elif v.color is l[0].color:
        assert False, 'FAIL'

def assign_color(v):
  if is_even(v.distance):
    v.color = color.green
  else:
    v.color = color.blue

def is_even(distance):
  return not distance % 2

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
  V = ['a', 'b', 'c', 'd', 'f', 'g']
  E = [('b', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'b'), ('d', 'b'), ('b', 'd'), ('f', 'd'), ('d', 'f'), ('f', 'g'), ('g', 'f')]
  A = adjacent_list(V, E)
  print('Adjacent list:')
  # print(A)
  breath_first_search(A, 'a')
  print(A)
  # print('\nPath from a to h:')
  # print_path(A, 'a', 'h')
