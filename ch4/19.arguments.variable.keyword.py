def func(**kwargs): #note: 가변인자가 dict 형태임
    print(kwargs)

# All calls equivalent. They print: {'a': 1, 'b': 42}
func(a=1, b=42)
func(**{'a': 1, 'b': 42}) #note: dict 형태를 unpack해서 넘겨즘
func(**dict(a=1, b=42))
