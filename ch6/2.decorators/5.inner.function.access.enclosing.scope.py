def compose_greet_func(name):
    def get_message():
        return "Hello there " + name + "!"  # note: inner 함수는 바로 위 scope 접근가능하다

    return get_message

greet = compose_greet_func("John")
print(greet())

# Outputs: Hello there John!
