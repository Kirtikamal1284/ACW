import numpy as np
import matplotlib.pyplot as plt

# Function to simulate the movement of a cell with 8 possible directions
def move_cell_8_directions(position, grid_size):
    
    # Randomly determine direction for row (x) and column (y)
    rand_x = int(np.random.uniform(0, 2))  # 0 or 1
    rand_y = int(np.random.uniform(0, 2))  # 0 or 1

    # Update row and column with boundary checks
    new_x = max(min(position[0] + (1 if rand_x == 0 else -1), grid_size - 1), 0)
    new_y = max(min(position[1] + (1 if rand_y == 0 else -1), grid_size - 1), 0)

    return new_x, new_y


# Get grid size and step count from user
grid_size = int(input("Enter grid size (e.g., 100): "))
steps = int(input("Enter number of steps (e.g., 10000): "))

# Initialize position and path for X and Y values
initial_position = (grid_size // 2, grid_size // 2)  # Start at grid center
position = initial_position
path = [position]  # List to track the path of the cell
move_count = 0  # Counter for total moves

# Simulate the movement
for _ in range(steps):
    position = move_cell_8_directions(position, grid_size)
    path.append(position)
    move_count += 1  # Increment the move counter for each step

# Extract X and Y coordinates for plotting
x_coords, y_coords = zip(*path)

# Plot the movement
plt.figure(figsize=(8, 8))
plt.plot(y_coords, x_coords, marker='o', markersize=2, linestyle='-', label="Cell Path")
plt.scatter(y_coords[0], x_coords[0], color="green", label="Start", s=50)  # Starting point
plt.scatter(y_coords[-1], x_coords[-1], color="red", label="End", s=50)  # Ending point
plt.xlim(0, grid_size)
plt.ylim(0, grid_size)
plt.gca().invert_yaxis()  # Invert y-axis for grid representation
plt.title(f"Movement of a Cell on a {grid_size}x{grid_size} Grid ({steps} Steps)")
plt.xlabel("Grid X")
plt.ylabel("Grid Y")
plt.legend()
plt.grid()
plt.show()

# Display total moves
print(f"Total number of moves: {move_count}")
