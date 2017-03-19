def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message #note: 함수를 반환한다

greet = compose_greet_func()
print(greet())

# Outputs: Hello there!
