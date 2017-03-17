import sys

def moddiv(a, b):
    return a // b, a % b  # note: multiple 값을 return하고 싶으면 tuple로

def test(n=10 ** 4):
    from random import choice, random, randint
    m = 10 ** 6
    for x in range(n):
        a = choice((randint(0, m), m * random()))
        b = 0
        while not b:
            b = choice((randint(1, m), m * random()))

        r = divmod(a, b)
        r2 = moddiv(a, b)
        if r != r2:
            print('Difference: ', a, b, r, r2)

if __name__ == "__main__":  # todo: 이건 어떻게 처리되나?
    test(10 ** 6)
    print('Done')

    print(moddiv(20, 7))  # prints (2, 6)

# test
print(5 * 2)  # 5 * 2 = 10
print(5 ** 2)  # 5^2 = 5 * 5 = 25
print("recursion call 할수 있는 limit: ", sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print("recursion call 할수 있는 limit: ", sys.getrecursionlimit())
