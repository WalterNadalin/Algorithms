from data_structures.adjacency_list import adjacency_list, color

t = 0
k = 0

def is_cyclic(A):
  global t
  global k

  for u in A:
    if u[0].color is color.white:
        if visit(A, u[0].key):
            print('There`s a cycle.')
            return

        k += 1

  print('No cycle.')

def visit(A, s):
  global t
  t += 1
  u = A.find(s)
  u[0].d = t
  u[0].cc = k
  u[0].color = color.grey

  for x in u[1:]:
      v = A.find(x)[0]

      if v.color is color.white:
        visit(A, v.key)
      elif v.color is color.black:
        return True

  u[0].color = color.black
  t += 1
  u[0].f = t
  return False


if __name__ == "__main__":
  V = ['a', 'b', 'c', 'd', 'e']
  E = [('b', 'a'), ('a', 'b'), ('a', 'c'), ('c', 'a'), ('d', 'c'), ('c', 'd'), ('e', 'd'), ('d', 'e'), ('e', 'b'), ('b', 'e')]
  A = adjacency_list(V, E)
  print('Adjacency list:')
  print(A)
  is_cyclic(A)
