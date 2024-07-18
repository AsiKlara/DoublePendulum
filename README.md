# double pendulum

Program visualises deterministic chaos of double pendulum system.
Depending on initial conditions and other parameters (such as mass or length)
the program calculates trajectory of n double pendulums which at the beginning
starts at the position differing by only a small fraction of radian.
Hamilton canonical equations of motion are solved numerically by runge-kutta classical
method (RK4). Visualisation and animation is created using matplotlib package.
Calculating more than 10 pendulums can be quite time-consuming, so you can see 
the animations precalculated as .mp4.
## installation

```commandline
pip install -r requirements.txt
```

## what you can change
- `n_pendulums` changes how many pendulums will be displayed recommended values 0 < number <= 100, number is required to be int
- `d_diff` recommended 0 < value < 0.1
- `t_max` is length of simulation 0 < time <= 20 (greater than 20 seconds is kinda pointless)
- `g` can be changed, but it's set to earth, so why changing it?
- `m1`, `m2`, `L1`, `L2` needs to be greater than 0
- `theta1`, `theta2` recommended value -1.57 < value < 1.57, 0 is equilibrium