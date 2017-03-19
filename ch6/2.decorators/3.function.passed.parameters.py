def greet(name):
    return "Hello " + name

def call_func(func): # note: 함수를 인자로 받을 수 있다
    other_name = "John"
    return func(other_name) 

print(call_func(greet))

# Outputs: Hello John
