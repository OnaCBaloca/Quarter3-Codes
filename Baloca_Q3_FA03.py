import numpy as np

names= ["Aston", "Marvoun", "Jane"]
days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
         [4500, 5200, 4800, 5000, 5300],
         [4000, 4100, 3900, 4200, 4600],
         [6000, 5800, 5900, 6100, 6200]
    ])

for i in range(len(names)):
    total_steps = np.sum(steps[i])
    average_steps = np.mean(steps[i])
    max_steps = np.max(steps[i])
    min_steps = np.min(steps[i])
    print(names[i], ":", steps[i])
    print(f"{names[i]}'s Step Summary:")
    print(f"  Total Steps: {total_steps}")
    print(f"  Average Daily Steps: {average_steps:.2f}")
    print(f"  Maximum Steps in a Day: {max_steps}")
    print(f"  Minimum Steps in a Day: {min_steps}\n")