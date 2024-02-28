from numpy.random import randint

def naive_pattern_matching(P, T):
  n = len(T)
  m = len(P)

  assert n > m, 'Lenght of the pattern greater than length of the text'

  shifts = []

  for s in range(n - m + 1):
    i = 0

    while i < m and T[s + i] == P[i]:
      i += 1

    if i == m:
      shifts += [s]

  return shifts

def compute_prefix(P):
  m = len(P)
  p = [0 for _ in range(m)]
  p[0] = 0
  k = 0

  for i in range(1, m):
    while k > 0 and P[i] != P[k]:
      k = p[k - 1]

    if P[i] == P[k]:
      k += 1

    p[i] = k

  return p

def knuth_morris_pratt(P, T):
  n = len(T)
  m = len(P)

  assert n > m, 'Lenght of the pattern greater than length of the text'

  p = compute_prefix(P)
  shifts = []

  ''' Book's algorithm
  q = 0

  for i in range(1, n):
    while q > 0 and P[q] != T[i]:
      q = p[q - 1]

    if P[q] == T[i]:
      q += 1

    if q == m:
      shifts += [i - m + 1]
      q = p[q - 1]

  ''' 

  s = 0

  while s <= n - m:
    q = 0

    while q < m and T[s + q] == P[q]:
      q += 1

    if q == m:
      shifts += [s]

    s += q - p[q - 1] if q > 0 else 1

  return shifts

if __name__ == '__main__':
  alphabet = 'a b c'.split()
  text_size = 50
  text_characters = randint(len(alphabet), size = text_size)
  text = [alphabet[i] for i in text_characters]
  pattern_size = 2
  pattern_characters = randint(len(alphabet), size = pattern_size)
  pattern = [alphabet[i] for i in pattern_characters]
  print('Text:', ''.join(text))
  print('Pattern:', ''.join(pattern))
  print('Pattern`s prefix function:', compute_prefix(pattern))
  print('Valid shifts n\u00e4ive algorithm:', naive_pattern_matching(pattern, text))
  print('Valid shifts Knuth-Morris-Pratt algorithm:', knuth_morris_pratt(pattern, text))

  S = 'x y z x w x u x y z x'.split()
  print(compute_prefix(S))
