# Taking input from user
set1 = set(input("Enter elements of the first set (comma separated): ").split(","))
set2 = set(input("Enter elements of the second set (comma separated): ").split(","))

# Convert input to integers (if needed, as input comes as strings)
set1 = {int(x) for x in set1}
set2 = {int(x) for x in set2}

# Set Operations
print("\nSet Operations:")

# Union
union_result = set1.union(set2)
print(f"\nUnion (set1 ∪ set2): {union_result}")

# Intersection
intersection_result = set1.intersection(set2)
print(f"\nIntersection (set1 ∩ set2): {intersection_result}")

# Difference
difference_result = set1.difference(set2)
print(f"\nDifference (set1 - set2): {difference_result}")

# Symmetric Difference
symmetric_difference_result = set1.symmetric_difference(set2)
print(f"\nSymmetric Difference (set1 Δ set2): {symmetric_difference_result}")

# Subset and Superset
print(f"\nIs set1 a subset of set2? {set1.issubset(set2)}")
print(f"\nIs set1 a superset of set2? {set1.issuperset(set2)}")

# Disjoint Sets
print(f"\nAre set1 and set2 disjoint? {set1.isdisjoint(set2)}")
