def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper

@p_decorate #note: decorate을 할 함수에 decorating하는 함수의 이름을 적으면 됨
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))

# previous #6
#my_get_text = p_decorate(get_text) note: <-- 이 부분이 대신
#print(my_get_text("John"))

# Outputs <p>lorem ipsum, John dolor sit amet</p>
