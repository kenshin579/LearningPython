def func(*args):
    print(args) # note:
    print(*args) # note: 가변인자(tuple)를 unpacking를 함

values = (1, 3, -7, 9)
func(1, 3, -7, 9)
func(values)  # equivalent to: func((1, 3, -7, 9))
func(*values)  # equivalent to: func(1, 3, -7, 9) note: values(tuple)를 unpacking해서 넘겨줌
