from suffix_tree import mccreight, is_empty, visualize

def longest_repeating_factor(text):
  root = mccreight(text)
  deepest = deepest_dfs(root)
  return text[deepest.start: deepest.start + deepest.depth]

def longest_3_repeating_factor(text):
  root = mccreight(text)
  count_leaves(root)
  root.count = 0
  deepest = deepest_3_dfs(root)
  return text[deepest.start: deepest.start + deepest.depth]

'''
def assign_length(node):
  root.length = 0
  compute_length(root)
  if is_empty(node.child):
    return node.parent, node.parent.depth

  deepest_depth = 0

  for child in node.child.values():
    temporary, child_depth = search_deepest(child)

    if child_depth > deepest_depth:
      deepest_depth += child_depth
      deepest = temporary

  return deepest, deepest_depth
'''

def deepest_dfs(root):
  maximum = 0
  deepest = root

  for v in root.child.values():
    if not is_empty(v.child):
      temp = deepest_dfs(v)

      if temp.depth > maximum:
        maximum = temp.depth
        deepest = temp

  return deepest

def deepest_3_dfs(root):
  maximum = 0
  deepest = root

  for v in root.child.values():
    if not is_empty(v.child):
      temp = deepest_3_dfs(v)

      if temp.depth > maximum and temp.count >= 3:
        maximum = temp.depth
        deepest = temp

  return deepest

'''
def count_children(root):
  Q = []
  Q += [root]

  while not is_empty(Q):
    cnrt = Q.pop(0) 
    cnrt.count = 0

    for v in cnrt.child.values():
      cnrt.count += 1
      Q += [v]

  root.count = 0
'''

def count_leaves(root):
  root.count = 0

  for v in root.child.values():
    if is_empty(v.child):
      root.count += 1
    else:
      root.count += count_leaves(v)

  return root.count

def compute_length(u):
  for v in u.child.values():
    v.length = v.depth + v.parent.length
    compute_length(v)

if __name__ == '__main__':
  text = "gigigione$"
  root = mccreight(text)

  print(f'The longest repeating factor of `{text}` is:') 
  print(longest_repeating_factor(text))

  print(f'The longest 3 times repeating factor of `{text}` is:') 
  print(longest_3_repeating_factor(text))
