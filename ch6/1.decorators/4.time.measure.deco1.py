from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func): # decorator
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)

    return wrapper #note: 함수를 반환함

f = measure(f)  # decoration point note: timing하는 부분이 f함수의 built-in 기능처럼 됨

f(0.2)  # f took: 0.2002875804901123
f(sleep_time=0.3)  # f took: 0.3003721237182617
print(f.__name__)  # wrapper  <- ouch!
