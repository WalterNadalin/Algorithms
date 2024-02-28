from suffix_tree import mccreight, is_empty

def suffix_array(node):
    SA = []

    if is_empty(node.child):
        return [node.start]

    for key, value in sorted(node.child.items()):
        SA += suffix_array(value)

    return SA

if __name__ == '__main__':
  text = "abbabbabbabbabaaabababbabbbabba$"
  root = mccreight(text)

  print('\nSuffix array:')
  for node in suffix_array(root):
    print(node)
