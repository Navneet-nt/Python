arr = [4, 5, 6, 1]
#print(sorted(set(arr), key=arr.count, reverse=True))
mapping = {val:i for i, val in enumerate(arr)}
print(mapping)