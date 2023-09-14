def decimal_to_binary(decimal):
    binary = []
    while decimal > 0:
        binary.append(decimal % 2)
        decimal //= 2
    return ''.join(str(bit) for bit in binary[::-1])

for i in range(256):
    print(decimal_to_binary(i))