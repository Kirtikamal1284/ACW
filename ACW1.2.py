import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Function to simulate the movement of a cell with 8 possible directions
def random_move_8_directions(position, steps, grid_size):
    path = [position]  # Store the path
    directions = []  # Store the directions

    # Define possible move (dx, dy)
    moves = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1),
        "Up-Left": (-1, -1),
        "Up-Right": (-1, 1),
        "Down-Left": (1, -1),
        "Down-Right": (1, 1),
    }

    for _ in range(steps):
        # Randomly select a direction
        direction = np.random.choice(list(moves.keys()))
        dx, dy = moves[direction]

        # Update position with boundary checks
        x = max(0, min(grid_size - 1, position[0] + dx))
        y = max(0, min(grid_size - 1, position[1] + dy))
        position = (x, y)
        path.append(position)

        # Record direction
        directions.append(direction)

    return path, directions

# Function to plot the movement
def plot_movement(path, title, grid_size):
    x_coords, y_coords = zip(*path)
    plt.figure(figsize=(8, 8))
    plt.plot(y_coords, x_coords, marker='o', markersize=1, linestyle='-', label="Path")
    plt.scatter(y_coords[0], x_coords[0], color="green", label="Start", s=40)  # Start
    plt.scatter(y_coords[-1], x_coords[-1], color="red", label="End", s=40)  # End
    plt.xlim(0, grid_size - 1)
    plt.ylim(0, grid_size - 1)
    plt.gca().invert_yaxis()  # Align grid orientation
    plt.title(title)
    plt.xlabel("Grid Y")
    plt.ylabel("Grid X")
    plt.legend()
    plt.grid()
    plt.show()

# Initial position
grid_size = 100
initial_position = (grid_size // 2, grid_size // 2)  # Start at the center

# Simulate and plot for 1000 steps
steps_1000 = 1000
path_1000, directions_1000 = random_move_8_directions(initial_position, steps_1000, grid_size)
plot_movement(path_1000, "Random Movement in 8 Directions: 1000 Steps", grid_size)

# Simulate and plot for 10,000 steps
steps_10000 = 10000
path_10000, directions_10000 = random_move_8_directions(initial_position, steps_10000, grid_size)
plot_movement(path_10000, "Random Movement in 8 Directions: 10,000 Steps", grid_size)

# Uniformity Analysis
direction_counts_1000 = Counter(directions_1000)
direction_counts_10000 = Counter(directions_10000)

print("Direction Counts for 1000 Steps:", direction_counts_1000)
print("Direction Counts for 10,000 Steps:", direction_counts_10000)
