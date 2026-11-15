import numpy as np
from common.domain.constants import (
    DT,
    V_MAX,
    MAX_STEER,
    STEER_RATE,
    ACCELEARTION_RATE,
    BRAKING_MAX,       
    DRAG,              
    WHEELBASE,         
)


class Car:

    # Kinematic bicycle model used here

    def __init__(self, x: float = 0.0, y: float = 0.0, heading: float = 0.0):
        self.x = x
        self.y = y
        self.heading = heading
        self.velocity = 0.0
        self.steer_angle = 0.0

    def reset(self, x: float = 0.0, y: float = 0.0, heading: float = 0.0):
        
        self.x = x
        self.y = y
        self.heading = heading
        self.velocity = 0.0
        self.steer_angle = 0.0

    def update(self, steer_cmd: float, throttle_cmd: float, brake_cmd: float, dt: float = DT):
        
        
        steer_target = steer_cmd * MAX_STEER
        steer_diff = steer_target - self.steer_angle
        max_steer_delta = STEER_RATE * dt
        self.steer_angle += np.clip(steer_diff, -max_steer_delta, max_steer_delta)

     
        accel = (
            throttle_cmd * ACCELEARTION_RATE
            - brake_cmd * BRAKING_MAX
            - DRAG * (self.velocity**2)
        )
        self.velocity = float(np.clip(self.velocity + accel * dt, 0.0, V_MAX))

       
        angular_velocity = (self.velocity / WHEELBASE) * np.tan(self.steer_angle)
        self.heading += angular_velocity * dt

        
        self.heading = (self.heading + np.pi) % (2.0 * np.pi) - np.pi

        
        self.x += self.velocity * np.cos(self.heading) * dt
        self.y += self.velocity * np.sin(self.heading) * dt

    def get_corners(self, length: float = 4.2, width: float = 1.8) -> np.ndarray:
      
        
        cos_h = np.cos(self.heading)
        sin_h = np.sin(self.heading)
        half_l = length / 2.0
        half_w = width / 2.0

        
        offsets = [
            (+half_l, +half_w), 
            (+half_l, -half_w), 
            (-half_l, -half_w), 
            (-half_l, +half_w), 
        ]

        corners = []
        for dx, dy in offsets:
            cx = self.x + (dx * cos_h - dy * sin_h)
            cy = self.y + (dx * sin_h + dy * cos_h)
            corners.append([cx, cy])

        return np.array(corners, dtype=np.float32)