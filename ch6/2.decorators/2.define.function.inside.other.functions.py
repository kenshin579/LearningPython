def greet(name):
    def get_message(): # note: 다른 함수안에 함수를 정의할 수 있다
        return "Hello "

    result = get_message() + name
    return result

print(greet("John"))

# Outputs: Hello John
