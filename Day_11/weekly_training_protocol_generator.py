import random

upper_Body = ["push_ups", "pull_ups", "overhead_press"]
lower_Body = ["weighted_squats", "deadlifts", "lunges"]
conditioning = ["Football_match", "sprints", "jump_rope"]
exercises = [upper_Body, lower_Body, conditioning]
training_days = ["Monday", "Wednesday", "Friday"]
for day in training_days:
    random_generation = random.choice(exercises[0])
    random_generation2 = random.choice(exercises[1])
    random_generation3 = random.choice(exercises[2])
    print(f"On {day}:")
    print(f"  - {random_generation}")
    print(f"  - {random_generation2}")
    print(f"  - {random_generation3}")
    print()