def try_syntax(numerator, denominator):
    try:
        print('In the try block: {}/{}'
              .format(numerator, denominator))
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else: # exception이 일어나자 읺았을 때
        print('The result is:', result)
        return result
    finally:
        print('Exiting')

print(try_syntax(12, 4))
print()
print(try_syntax(11, 0))
