# Roll a dice 10 times using random.randint() and count how many times you get 6.
import random

random.seed(42)

def count_sixes():
    count = 0
    for i in range(10):
        roll = random.randint(1, 6)
        print("Roll", i+1, "=", roll)
        if roll == 6:
            count += 1
    return count

total = count_sixes()
print("Number of times 6 appeared:", total)