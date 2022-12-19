import numpy as np

NUM_PLAYERS = 10
NUM_LEVELS = 5

base_churn_aps = np.random.randint(low=8, high=15, size=(NUM_LEVELS, 1), dtype=np.int16)
base_aps = np.random.randint(low=1, high=10, size=(NUM_LEVELS, 1), dtype=np.int16)
success_probs = 1 / np.tile(base_aps, (1, NUM_PLAYERS))
simulated_aps = np.random.geometric(p=success_probs, size=(NUM_LEVELS, NUM_PLAYERS))

tmp = simulated_aps > base_churn_aps
churned_players = (tmp.max(axis=0) * np.ones((NUM_PLAYERS)))[:, np.newaxis]
churned_levels = (tmp.argmax(axis=1) > 1)[:, np.newaxis]

print("Simulation end.")