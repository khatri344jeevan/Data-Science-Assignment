data = [12,15,18,20,22,25,27,30,32,35,
        38,40,42,45,48,50,52,55,58,60]
def calculate_mean(data):
    total = sum(data)
    count = len(data)
    return total / count
def calculate_median(data):
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]
        
def calculate_quartile(position, data):
    if position == int(position):
        return data[int(position) - 1]
    
    else:
        lower = data[int(position) - 1]
        upper = data[int(position)]
        return (lower + upper) / 2


data.sort()
N = len(data)

mean = calculate_mean(data)

median = calculate_median(data)

q1_position = (N + 1) / 4
q2_position = (N + 1) / 2
q3_position = 3 * (N + 1) / 4

q1 = calculate_quartile(q1_position, data)
q2 = calculate_quartile(q2_position, data)
q3 = calculate_quartile(q3_position, data)

iqr = q3 - q1

print("Mean:", mean)
print("Median (Q2):", median)
print("Q1:", q1)
print("Q3:", q3)
print("Interquartile Range:", iqr)