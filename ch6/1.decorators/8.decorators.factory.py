from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold: #note:
                print(
                    'Result is too big ({0}). Max allowed is {1}.'
                        .format(result, threshold))
            return result

        return wrapper

    return decorator

'''
note: 변수 값을 가지도록 함 (decorator factory) -> cube = max_result(75)(cube)
closure에 의해서 계속 75값을 기억을 하고 있음.
'''
@max_result(75)
def cube(n):
    return n ** 3

@max_result(100)
def square(n):
    return n ** 2

@max_result(1000)
def multiply(a, b):
    return a * b

print(cube(5))
