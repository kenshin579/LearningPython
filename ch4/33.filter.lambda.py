def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n))) #note: def func_name(k) : return not k % 5

print(get_multiples_of_five(50))
