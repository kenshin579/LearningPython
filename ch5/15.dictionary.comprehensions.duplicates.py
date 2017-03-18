word = 'Hello'

swaps = {c: c.swapcase() for c in word}

print(swaps)  # prints: {'o': 'O', 'l': 'L', 'e': 'E', 'H': 'h'}

# test
print(word.swapcase()) # 대문자 -> 소문자, 소문자->대문자
