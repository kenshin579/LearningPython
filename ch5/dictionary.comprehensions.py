from string import ascii_lowercase

lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
# lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}


from pprint import pprint

pprint(lettermap)
# print(lettermap)

# test
for i, name in enumerate(['body', 'foo', 'bar'], 1):
    print(i, name)
# 1 body
# 2 foo
# 3 bar