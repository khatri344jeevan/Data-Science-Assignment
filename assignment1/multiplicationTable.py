# Print a multiplication table for a number, but highlight the multiples of 5
def mul_table(n):
    print(f"Multiplication Table for {n}:")
    for i in range(1, 11):
        result = n * i
        if result % 5 == 0:
            print(result,"=multiple of 5")
        else:
            print(result)