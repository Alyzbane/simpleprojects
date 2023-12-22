import numpy as np
import os
import time
import random

DEAD = 0
ALIVE = 1


def load_board_state(s):
    with open(s, 'r') as f:
        lines = f.readlines()
    lines = [list(map(int,list(line.strip()))) for line in lines]

    return np.array(lines)

def dead_state(width, height):
    return np.full((width, height), DEAD)

# Initialize the board with random pattern
def random_state(width, height, threshold=None):
    # Default Initialization
    state = dead_state(width, height)
    if threshold is not None:
        threshold = threshold
    else:
        threshold = 0.9

    # Initialize the randomness of states
    rand_state = np.random.rand(*state.shape)
    # Define the randomness of value(0,1) for each cells
    state =  np.where(rand_state >= threshold, 0, 1) 

    # Defining the 'Soup'
    return state

def render(state):
    alive_block = '\u2588'
    dead_block = ' '
    # Define the rendered grid of states
    rendered_board = np.where(state == ALIVE, alive_block, dead_block)

    # Pretty print the cells
    for row in rendered_board:
        print(''.join([char*3 for char in row]))

def next_board_state(initial_state):
    rows, cols = initial_state.shape
    new_state = dead_state(rows, cols)

    # Defines the new state of the board
    for iy, ix in np.ndindex(initial_state.shape):
        neighbors = []
        for i in range(max(0, iy - 1), min(rows, iy + 2)):
            for j in range(max(0, ix - 1), min(cols, ix + 2)):
                if (i, j) != (iy, ix):
                    neighbors.append(initial_state[i, j])
        lives = sum(neighbors)
        # Define the assignment of neighbor state
        if initial_state[iy, ix] == ALIVE and (lives == 2 or lives == 3):
            new_state[iy, ix] = ALIVE
        elif initial_state[iy, ix] == DEAD and (lives == 3):
            new_state[iy, ix] = ALIVE
    return new_state

w = 20
h = 500

starting_state = load_board_state('frog.txt')
render(starting_state)
for i in range(100):
    time.sleep(0.4)
    #os.system('cls')
    starting_state = next_board_state(starting_state)
    render(starting_state)
