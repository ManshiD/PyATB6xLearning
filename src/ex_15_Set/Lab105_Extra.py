squares = {x ** 2 for x in range(5)}
print(squares)

# Frozen Set (Immutable Set)
# A frozenset cannot be changed after creation.

fset = frozenset([1, 2, 3, 3])
print(fset)
# fset.add(4) # AttributeError: 'frozenset' object has no attribute 'add'
