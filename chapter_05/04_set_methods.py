s = {10, 20, 30, 3, 10, "Israfil"}

print(s)

s.add(555)

print(s)

s.remove("Israfil")
print(s)

poped_item = s.pop()
print(poped_item)
print(s)

another_set = {20, 30, 55, 85, 47}

union_set = s.union(another_set)

print(union_set)

intersection_set = s.intersection(another_set)
print(intersection_set)