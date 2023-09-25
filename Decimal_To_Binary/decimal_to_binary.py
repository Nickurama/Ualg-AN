def decimal_to_binary(x):
    result = x
    if x >= 2:
        result = str(decimal_to_binary(x // 2)) + str(x % 2)
    return result


for i in range(64):
    print(f"{i}: {decimal_to_binary(i)}")
