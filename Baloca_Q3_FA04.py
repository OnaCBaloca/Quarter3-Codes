import numpy as np

names= ["Aston", "Marvoun", "Jane"]
days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
         [4500, 5200, 4800, 5000, 5300],
         [4000, 4100, 3900, 4200, 4600],
         [6000, 5800, 5900, 6100, 6200]
    ])

total_steps = np.sum(steps, axis=1)

high_tots = np.max(total_steps)
low_tots = np.min(total_steps)
highest_index = np.argmax(total_steps)

print("Total steps per person:")
for i in range(len(names)):
    print(names[i], ":", total_steps[i])

print("\nPerson with the highest total steps:")
print(names[highest_index], "with", high_tots, "steps")

print("\nDifference between highest and lowest total steps:")
print(high_tots - low_tots)