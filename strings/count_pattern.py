from suffix_tree import mccreight, is_empty, search

def count(pattern, root, text):
  pattern = [character for character in pattern]
  depth = 0
  node = root

  while not is_empty(pattern):

    if depth > node.depth - 1:
      node = node.child.get(pattern[0], None)

      if node is None:
        break

    if pattern[0] == text[node.start + depth]:
      pattern.pop(0)
    else:
      break

    depth += 1

  if is_empty(pattern):
    return node.count
  else:
    return 0

def assign_count(root):
  if is_empty(root.child):
    root.count = 1
    return root.count
  else:
    root.count = 0

  for child in root.child.values():
    count = assign_count(child)
    root.count += count

  return root.count

if __name__ == '__main__':
  text = "mississippi$"

  root = mccreight(text)
  assign_count(root)

  pattern = "i"
  print(f'\nThe pattern `{pattern}` appears in `{text}`', end = ' ')
  print(count(pattern, root, text), end = ' ')
  print(f'times.\nIndeed, the pattern `{pattern}` appears in `{text}` at position(s):')
  print(search(pattern, root, text))


  pattern = "ssi"
  print(f'\nThe pattern `{pattern}` appears in `{text}`', end = ' ')
  print(count(pattern, root, text), end = ' ')
  print(f'times.\nIndeed, the pattern `{pattern}` appears in `{text}` at position(s):')
  print(search(pattern, root, text))
