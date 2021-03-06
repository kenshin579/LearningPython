def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))

        return func_wrapper

    return tags_decorator

@tags("p") #note: wrap with a p string
def get_text(name):
    return "Hello " + name

print(get_text("John"))

# Outputs <p>Hello John</p>

# debugging decorated functions
print(get_text.__name__) # func_wrapper (get_text이 아니라) -> #12에서 functools 참조
