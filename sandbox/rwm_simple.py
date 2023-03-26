import numpy as np
from numpy import tile, ones, newaxis, int16 as np_int16
from numpy.random import randint, geometric

NUM_PLAYERS = 10
NUM_LEVELS = 5

base_churn_aps = randint(low=8, high=15, size=(NUM_LEVELS, 1), dtype=np_int16)
base_aps = randint(low=1, high=10, size=(NUM_LEVELS, 1), dtype=np_int16)
success_probs = 1 / tile(base_aps, (1, NUM_PLAYERS))
simulated_aps = geometric(p=success_probs, size=(NUM_LEVELS, NUM_PLAYERS))

tmp = simulated_aps > base_churn_aps
churned_players = (tmp.max(axis=0) * ones((NUM_PLAYERS)))[:, newaxis]
churned_levels = (tmp.argmax(axis=1) > 1)[:, newaxis]

print("Simulation end.")