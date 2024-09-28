import numpy as np # type: ignore

# Plate parameters
plate_size = 15  # in cm
grid_size = 5    # in cm
n = int(plate_size / grid_size) + 1  # number of grid points

# Boundary conditions
top_temp = 100.0
bottom_temp = 0.0
left_temp = 100.0
right_temp = 0.0

# Create a grid of temperatures
T = np.zeros((n, n))

# Set the boundary conditions
T[0, :] = top_temp        # Top boundary
T[-1, :] = bottom_temp    # Bottom boundary
T[:, 0] = left_temp       # Left boundary
T[:, -1] = right_temp     # Right boundary

# Parameters for convergence
tolerance = 1e-4
max_iterations = 1000

# Perform the iterative calculation
for iteration in range(max_iterations):
    T_old = T.copy()
    for i in range(1, n-1):
        for j in range(1, n-1):
            T[i, j] = 0.25 * (T_old[i+1, j] + T_old[i-1, j] +
                              T_old[i, j+1] + T_old[i, j-1])
    
    # Check for convergence
    if np.all(np.abs(T - T_old) < tolerance):
        print(f"Converged after {iteration+1} iterations.")
        break
else:
    print("Did not converge within the maximum number of iterations.")

# Print the steady-state temperature distribution
print("Steady-state temperature distribution:")
print(T)
