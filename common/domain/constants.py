DT = 1.0/30.0  # 30 Hz ocontrol frequency 

MAX_STEER= 0.5  # Max steering angle in radian

STEER_RATE=2.0  # Max steering rate in radian / sec

ACCELEARTION_RATE=8.0 # Max acceleration rate

BRAKING_MAX = 14.0 # Max braking rate

DRAG = 0.002 # AERODYNAMIC DRAG

V_MAX= 30.0  # Max speed 

WHEELBASE = 2.5 # Distance between front and rear wheel


# TRACK CONSTANTS AND DIMENSIONS

SCALE = 10.0 # 1 METER = 10 PIXELS
TRACK_WIDTH = 12.0 # Track width in meters
HALF_TRACK_WIDTH = TRACK_WIDTH / 2.0 # Half track width in meters

#RL LIMITS 
MAX_EPISODE_STEPS = 2000 # Max steps in an episode

STALL_STEP = 90 # Max steps in which car is not moving