import numpy as np

names= ["Aston", "Marvoun", "Jane"]
days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
         [4500, 5200, 4800, 5000, 5300],
         [4000, 4100, 3900, 4200, 4600],
         [6000, 5800, 5900, 6100, 6200]
    ])

daily_tots = np.sum(steps, axis=0)

print("Total steps per day:")
for i in range(len(days)):
    print(days[i], ":", daily_tots[i])

most_act_index = np.argmax(daily_tots)

print("\nMost active day overall:")
print(days[most_act_index], "with", daily_tots[most_act_index], "steps")