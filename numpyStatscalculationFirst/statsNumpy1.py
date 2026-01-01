import numpy as np

data = [12,15,18,20,22,25,27,30,32,35,38,40,42,45,48,50,52,55,58,60]

mean = np.mean(data)
median = np.median(data)

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)

iqr = q3 - q1

print("Mean:", mean)
print("Median (Q2):", median)
print("Q1:", q1)
print("Q3:", q3)
print("Interquartile Range:", iqr)