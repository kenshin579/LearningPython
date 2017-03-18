# items = 'ABCDE'
items = 'ABC'
pairs = []

# listing all pairs without duplication
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

print(pairs)
