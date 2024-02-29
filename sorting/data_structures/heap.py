from math import ceil, log2, floor

class heap:
	"""
	A (binary) heap data structure.
	"""
	def __init__(self, *args, max_heap = False):
		self.array = list(args)
		self.max_heap = max_heap

		if self.max_heap == True:
		    self.relation = lambda x, y: x >= y
		else:
		    self.relation = lambda x, y: x <= y

		self.build_heap()

	def __str__(self, index = 0, level = 0):
		right = self.right(index)
		left = self.left(index)
		string = self.__str__(right, level + 1) if self.is_valid(right) else ''
		string += '\t' * level + str(self.array[index]) + '\n'
		string += self.__str__(left, level + 1) if self.is_valid(left) else ''
		return string

	def __repr__(self):
		string = f'{self.__class__.__name__}('
		string += ', '.join([str(node) for node in self.array])

		if self.max_heap == True:
		    string += ', max_heap = ' + str(self.max_heap) + ')'
		else:
		    string += ')'

		return string 

	def __getitem__(self, index):
		return self.array[index]

	def __eq__(self, other):
		return self.array == other.array

	def __len__(self):
		return len(self.array)

	def get_last(self):
		return len(self) - 1

	def is_valid(self, i):
		return i < len(self)

	def get_root(self):
		return 0

	def is_root(self, i):
		assert self.is_valid(i), 'Element out of bound.'
		return i == self.get_root()

	def left(self, i):
		assert self.is_valid(i), 'Element out of bound.'
		return 2 * i + 1

	def right(self, i):
		assert self.is_valid(i), 'Element out of bound.'
		return 2 * i + 2

	def parent(self, i):
		assert self.is_valid(i), 'Element out of bound.'
		return ceil(i / 2) - 1

	def minimum(self):
		return self.array[self.get_root()]

	def maximum(self):
		return self[self.find_maximum()]

	def delete_maximum(self):
		maximum = self.find_maximum()
		last = self[self.get_last()]

		if self[maximum] > last:
		    self.decrease(maximum, last)

		self.array.pop(-1)

	def find_maximum(self):
		maximum = len(self) // 2
		i = maximum + 1

		while self.is_valid(i):
		    if self[maximum] < self[i]:
		        maximum = i

		    i += 1

		return maximum

	def pop_minimum(self):
		self.array[0], self.array[-1] = self.array[-1], self.array[0]
		minimum = self.array.pop(-1)
		self.heapify(0)
		return minimum

	def heapify(self, i):
		assert self.is_valid(i), 'Element out of bound.'
		tmp = i

		for index in (self.left(i), self.right(i)):
		    if self.is_valid(index) and self.relation(self.array[index], self.array[tmp]):
		        tmp = index

		if i != tmp:
		    self.array[i], self.array[tmp] = self.array[tmp], self.array[i]
		    self.heapify(tmp)

	def build_heap(self):
		last = self.get_last()
		for index in [i for i in range(self.parent(last), -1, -1)]:
		    self.heapify(index)

	def decrease(self, i, value):
		assert self.is_valid(i), 'Element out of bound.'
		if self.max_heap == True:
		    self.array[i] += value
		else:
		    self.array[i] -= value

		while not self.is_root(i) and self.relation(self.array[i], self.array[self.parent(i)]):
		    parent = self.parent(i)
		    self.array[i], self.array[parent] = self.array[parent], self.array[i]
		    i = parent

	def insert(self, value):
		last = self.get_last() 
		self.array += [self.array[last]]
		last = self.get_last()
		self.decrease(last, abs(value - self.array[last]))

if __name__ == "__main__":
	H = heap(0, 1, 2, 3)
