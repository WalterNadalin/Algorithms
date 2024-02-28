from adjacent_list import adjacent_list, color, empty_queue

t = 0
k = 0

def depth_first_search(A):
  global t
  global k

  for u in A:
    if u[0].color is color.white:
      visit(A, u[0].key)
      k += 1

def visit(A, s):
  global t
  t += 1
  u = A.find(s)
  u[0].d = t
  u[0].cc = k
  u[0].color = color.grey

  for x in u[1:]:
      v = A.find(x)[0]

      if v.count > 1:
        assert False, 'The DAG is not a tree'

      if v.color is color.white:
        visit(A, v.key)

  u[0].color = color.black
  t += 1
  u[0].f = t


if __name__ == "__main__":
  V = [1, 2, 3]
  E = [(2, 1), (3, 1), (3, 2)]
  A = adjacent_list(V, E)
  print('Adjacent list:')
  print(A)
  depth_first_search(A)

  for x in A:
    print(f'{x[0]}: ({x[0].d}, {x[0].f}), {x[0].cc}')
