
"""
Recovery

k_p Proportional gain: multiplies lateralOffset (distance from the center) to steer the car toward the middle of the road.
k_d Derivative gain:  multiplies headingError (angle relative to the road) to straighten the car out so it does not overshoot the center and wobble.
"""

k_p = 0.6
k_d = 0.5