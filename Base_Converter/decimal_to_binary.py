def decimal_to_binary(x):
    if x >= 2:
        x = str(decimal_to_binary(x // 2)) + str(x % 2)
    return x


for i in range(64):
    print(f"{i}: {decimal_to_binary(i)}")
