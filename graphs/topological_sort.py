from depth_first_search import depth_first_search
from data_structures.adjacency_list import adjacency_list

def topological_sort(A):
  depth_first_search(A)
  V = [x[0] for x in A]
  n = len(V)

  for i in reversed(range(n)):
    for j in range(n - 1):
      if V[j].f > V[j + 1].f:
        V[j], V[j + 1] = V[j + 1], V[j]

  return V[::-1]

if __name__ == "__main__":
  V = ['watch', 'pants', 'socks', 'shoes', 'tie', 'underwear', 'coat', 'shirt', 'belt']
  E = [('pants', 'underwear'), ('shoes', 'underwear'), ('shoes', 'socks'), ('shoes', 'pants'), ('belt', 'pants'), ('belt', 'shirt'), ('tie', 'shirt'), ('coat', 'tie'), ('coat', 'belt')]
  A = adjacency_list(V, E)
  print('Adjacency list:')
  print(A)
  print('\nTopological sort:')
  print(topological_sort(A))
