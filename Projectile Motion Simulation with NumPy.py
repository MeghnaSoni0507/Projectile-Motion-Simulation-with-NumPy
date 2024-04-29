import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(initial_velocity, launch_angle, gravity=9.8, time_step=0.1, total_time=10):
    """
    Simulate projectile motion and return the x and y coordinates over time.
    
    Parameters:
    - initial_velocity: Initial velocity of the projectile (m/s)
    - launch_angle: Launch angle in degrees
    - gravity: Acceleration due to gravity (m/s^2)
    - time_step: Time step for simulation (s)
    - total_time: Total time for the simulation (s)
    
    Returns:
    - x_coordinates: Array of x coordinates over time
    - y_coordinates: Array of y coordinates over time
    """
    # Convert launch angle to radians
    launch_angle_rad = np.radians(launch_angle)
    
    # Calculate the initial components of velocity
    initial_velocity_x = initial_velocity * np.cos(launch_angle_rad)
    initial_velocity_y = initial_velocity * np.sin(launch_angle_rad)
    
    # Calculate the time points
    time_points = np.arange(0, total_time, time_step)
    
    # Calculate the x and y coordinates over time
    x_coordinates = initial_velocity_x * time_points
    y_coordinates = initial_velocity_y * time_points - 0.5 * gravity * time_points**2
    
    return x_coordinates, y_coordinates

# Set up the simulation parameters
initial_velocity = 20  # m/s
launch_angle = 45      # degrees

# Run the projectile motion simulation
x_coords, y_coords = projectile_motion(initial_velocity, launch_angle)

# Plot the trajectory
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, label=f'Launch Angle: {launch_angle}°')
plt.title('Projectile Motion Simulation')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.legend()
plt.grid(True)
plt.show()
