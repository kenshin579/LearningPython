items = 'ABCDE'
pairs = [(items[a], items[b]) #note: loop body
         for a in range(len(items)) for b in range(a, len(items))] #note: outer, inner loop

print(pairs)
