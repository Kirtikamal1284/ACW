import numpy as np
import matplotlib.pyplot as plt
#Part 1.1
# Function to simulate the movement of the grey cell
def move_cell(position, grid_size):
   
    # Generate random values (0 or 1) for movement directions
    rand_x = int(np.random.uniform(0, 2))  
    rand_y = int(np.random.uniform(0, 2))  

    # Apply movement rules based on random values
    if rand_x == 1 and rand_y == 1:
        # Move up (row decreases)
        new_position = (max(position[0] - 1, 0), position[1])
    elif rand_x == 1 and rand_y == 0:
        # Move down (row increases)
        new_position = (min(position[0] + 1, grid_size - 1), position[1])
    elif rand_x == 0 and rand_y == 1:
        # Move left (column decreases)
        new_position = (position[0], max(position[1] - 1, 0))
    else:  # rand_x == 0 and rand_y == 0
        # Move right (column increases)
        new_position = (position[0], min(position[1] + 1, grid_size - 1))

    return new_position


# Simulation parameters
grid_size = 100  
initial_position = (grid_size // 2, grid_size // 2)  # Start in the middle of the grid
num_steps = 100  
# Initialize cell position and path
position = initial_position
path = [position]  # List to store the path of the cell

# Simulate cell movement
for _ in range(num_steps):
    position = move_cell(position, grid_size)
    path.append(position)

# Extracttion of the X and Y coordinates for plotting
x_coords, y_coords = zip(*path)

# Plotting the movement of the cell
plt.figure(figsize=(8, 8))
plt.plot(y_coords, x_coords, marker='o', markersize=3, linestyle='-', label="Cell Path")
plt.scatter(y_coords[0], x_coords[0], color="green", label="Start", s=30, zorder=5)  # Starting point
plt.scatter(y_coords[-1], x_coords[-1], color="red", label="End", s=30, zorder=5)  # Ending point
plt.xlim(0, grid_size)
plt.ylim(0, grid_size)
plt.gca().invert_yaxis()  # Invert y-axis to align with grid representation
plt.title("Movement of a Cell on a 100x100 Grid")
plt.xlabel("Grid X")
plt.ylabel("Grid Y")
plt.legend()
plt.grid()
plt.show()
