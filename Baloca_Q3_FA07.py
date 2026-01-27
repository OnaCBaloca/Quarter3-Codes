import numpy as np

names = ["Aston", "Marvoun", "Jane"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

print("Daily Steps per Person:\n")
for i in range(len(names)):
    print(names[i], ":", steps[i])

print("\nSummary:\n")
for i in range(len(names)):
    total_steps = steps[i].sum()
    average_steps = steps[i].mean()
    print(names[i])
    print(" Total steps:", total_steps)
    print(" Average steps:", average_steps)
    print()

print("Overall Maximum Steps:", steps.max())
print("Overall Minimum Steps:", steps.min())

#How did using an array help you analyze the data more easily?
#Arrays allow for efficient storage and manipulation of multi-dimensional data, making it easier to perform calculations like sums and averages across multiple rows or columns.

#Which part of summarizing the data was easy or difficult?
#Calculating totals and averages was straightforward using array methods. However, ensuring the correct indexing for each person required careful attention.
