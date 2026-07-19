# s= {1,2,3,4,5,5,4,4,"inaam"} 
# print(s,type(s))
# s.add(444)
# print(s,type(s))
# 🔁 Adding and Removing Elements
# add(elem): Adds an element to the set.

# update(iterable): Adds multiple elements (from a list, tuple, etc.).

# remove(elem): Removes an element. Raises KeyError if not found.

# discard(elem): Removes an element, but doesn't raise an error if not found.

# pop(): Removes and returns a random element.

# clear(): Removes all elements from the set.

# 🔍 Set Operations
# union(*others) or |: Returns a new set with all elements from the sets.

# intersection(*others) or &: Returns elements common to all sets.

# difference(*others) or -: Elements in the set but not in others.

# symmetric_difference(other) or ^: Elements in either set, but not both.

# 🧪 Set Comparison
# issubset(other) or <=: Checks if all elements of this set are in the other.

# issuperset(other) or >=: Checks if this set contains all elements of the other.

# isdisjoint(other): Checks if sets have no elements in common.

# 🧬 Copying
# copy(): Returns a shallow copy of the set.

# 🧠 Quick Example

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))         # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))    # {1, 2}
print({1,2}.issubset(a))
print({1,2}.issuperset(a))