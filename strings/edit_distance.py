def compare(i, j):
    return 0 if S[i - 1] == T[j - 1] else 1

def aux_edit_matrix(T, S, k = 0):
    n = len(T) + 1
    m = len(S) + 1
    k = k if k else max(n, m)
    cost = 1

    matrix = [[(cost * i, 0) if j == 0 else [0, 0] for j in range(n)] for i in range (m)]
    matrix[0] = [(cost * j, 0) for j in range(n)]

    for i in range(1, m):
        for j in range(1, n):
          if i - k <= j <= i + k:
            matrix[i][j] = min({matrix[i - 1][j][0] + cost: 1, \
                                matrix[i][j - 1][0] + cost: 2, \
                                matrix[i - 1][j - 1][0] +   \
                                compare(i, j): 3}.items(),  \
                                key = lambda x: x[0])

    return matrix

def edit_matrix(T, S):
  k = 10
  matrix = aux_edit_matrix(T, S, k)

  while matrix[-1][-1][0] >= k:
    k *= 2
    matrix = aux_edit_matrix(T, S, k)

  return matrix

def edit_transcript(T, S):
    matrix = edit_matrix(T, S)
    i = len(S)
    j = len(T)

    transcript = ''

    while i != 0 and j != 0:
        if matrix[i][j][1] == 2:
            transcript += 'D'
            j -= 1
        elif matrix[i][j][1] == 1:
            transcript += 'I'
            i -= 1
        else:
            transcript += 'R' if compare(i, j) else 'M'
            i -= 1
            j -= 1

    if i == 0:
      while j != 0:
        transcript += 'D'
        j -= 1
    elif j == 0:
      while i != 0:
        transcript += 'I'
        i -= 1

    return transcript[::-1]

def edit_distance(T, S):
    return edit_matrix(T, S)[-1][-1][0]

T = "zyu"
S = "xyzuw"

print(f'{T = }\n{S = }')
#print('Edit matrix:')

# for row in edit_matrix(T, S):
#    print(row)

for x in edit_matrix(T, S):
  print(x)

print('Edit distance:', edit_distance(T, S))
print('Edit transcript:', edit_transcript(T, S))
