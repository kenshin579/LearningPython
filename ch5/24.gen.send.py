def counter(start=0):
    n = start
    while True: #note: result는 c.send()할때 다시 값을 받을 수 있는 변수임
        result = yield n # A: execution stops and n(0) is yielded back to the caller
        print(type(result), result) # B:
        if result == 'Q':
            break
        n += 1

c = counter()
print(next(c)) # C: while으로 들어감 #A에서 stops
print(c.send('Wow!'))  # D: execution resumes and result is set to 'Wow!' and prints 1
print(next(c)) # E
print(c.send('Q'))  # F
