from dataclasses import dataclass


@dataclass
class PhysicalAction:
    steer: float # Angle between front wheel and body of car in radians
    throttle: float # Throttle value between 0.0 and 1.0
    brake: float # Brake value between 0.0 and 1.0
