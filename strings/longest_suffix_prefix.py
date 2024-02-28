from pattern_matching import compute_prefix

def longest_suffix_prefix(text):
  p = compute_prefix(text)
  print(p)
  return p[-1]

if __name__ == '__main__':
  text = "abbabbabbabbabaaabababbabbabba"

  print(f'The longest prefix-suffix of {text} is:')

  k = longest_suffix_prefix(text)

  if k == 0:
    print('A prefix-suffix don`t exists.')
  else:
    print(text[0:k])
