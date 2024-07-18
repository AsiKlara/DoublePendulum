# Double Pendulum Simulation Documentation

## Overview

Program visualises deterministic chaos of double pendulum system.
Depending on initial conditions and other parameters (such as mass or length) the program calculates trajectory of n
double pendulums which at the beginning starts at the position differing by only a small fraction of radian.
Hamilton canonical equations of motion are solved numerically by runge-kutta classical method (RK4).
Visualisation and animation is created using matplotlib package.
Calculating more than 10 pendulums can be quite time-consuming, so you can see the animations precalculated as .mp4.

## Initialization

### Constants and Parameters
- `n_pendulums`: Number of pendulums in the simulation.
- `d_diff`: Small degree difference between initial angles of pendulums.
- `g`: Gravitational acceleration (constant).
- `m1`, `m2`: Masses of the pendulums.
- `L1`, `L2`: Lengths of the pendulum rods.
- `theta1`, `theta2`: Initial deflection angles of the pendulums.
- `p1_n`, `p2_n`: Initial momenta of the pendulums.
- `dt`: Time step for the simulation.
- `t_max`: Total simulation time.
- `n_steps`: Number of simulation steps.

### Initial Conditions
- Initialize arrays for storing angles (`theta1_arr`, `theta2_arr`) and time (`t_arr`).
- Initialize momenta (`p1`, `p2`) and apply small differences to initial angles for each pendulum.

## Hamiltonian Equations of Motion

### Functions for Equations of Motion
- `theta1_dot(p1, p2, theta1, theta2, L1, L2)`: Computes the rate of change of `theta1`.
- `theta2_dot(p1, p2, theta1, theta2, L1, L2)`: Computes the rate of change of `theta2`.
- `p1_dot(p1, p2, theta1, theta2, L1, L2)`: Computes the rate of change of `p1`.
- `p2_dot(p1, p2, theta1, theta2, L1, L2)`: Computes the rate of change of `p2`.

## Numerical Integration

### Runge-Kutta Method
- `runge_kutta(n_steps, dt, t_arr, theta1_arr, theta2_arr, p1, p2, L1, L2, n_pendulums)`:
Solves the equations of motion using the classical Runge-Kutta (RK4) method.
  - Iterates through each time step and computes new values of angles and momenta.
  - Saves the computed results in the respective arrays.

## Conversion to Cartesian Coordinates

### Coordinate Transformation
- `back_to_cartesian(theta1_arr, theta2_arr, L1, L2, n_steps, n_pendulums)`: Converts angular results to Cartesian coordinates.
  - Returns arrays of x and y coordinates for both masses of each pendulum.

## Animation

### Visualization
- `animace(x1, y1, x2, y2, n_steps, dt, n_pendulums)`: Animates the motion of the double pendulums.
  - Sets up the figure and axes for the animation.
  - Uses a colormap to differentiate pendulums.
  - Updates the positions of the pendulum rods and masses in each frame.
  - Optionally saves the animation as an MP4 file.

## Execution
- Execute the simulation by running the Runge-Kutta method to solve the equations of motion.
- Convert the results to Cartesian coordinates.
- Animate the motion of the pendulums to visualize their trajectories.

This simulation demonstrates the complex and chaotic behavior of double pendulums,
highlighting the sensitivity to initial conditions.
The visualization provides an engaging way to observe the dynamic motion of the system.