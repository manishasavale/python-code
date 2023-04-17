#set is mutable sequence univocal(without repetitions) unordered
# frozenset is immutable
# Data sets
s1 = set(range(3))
s2 = set(range(10,7,-1))
s3 = set(range(2, 10, 2))

# shows the data
print('s1:', s1, '\ns2:', s2, '\ns3:', s3)


# Union

s1s2 = s1.union(s2) 
print('Union of set s1 and set s2', s1s2)

# difference
print('Defference with s3:', s1s2.difference(s3))

#intersection
print('Intersection with s3:', s1s2.intersection(s3))

#Tests if a set includes the other
if s1.issuperset([1, 2]):
    print('s1 includes 1 and 2')

# Tests if there is no common elements
if s1.isdisjoint(s2):
    print('s1 and s2 have no common elements')
