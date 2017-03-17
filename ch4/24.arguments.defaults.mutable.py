def func(a=[], b={}): #note: 이런 mutable default 값은 주의를 해라 (하지만 memoization 기술로 사용됨
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))  # this will affect a's default value
    b[len(a)] = len(a)  # and this will affect b's one

func()
func()
func()
