from dataclasses import dataclass
import numpy as np


@dataclass
class SensorReading:
    """
    Attributes:
    speed: speed of car in meters/second 
        Raw Range [0, 30] m/s
        Normalised Range [0, 1] 
    
    steer: Angle between front wheel and body of car in radians
        Raw Range [-0.5, 0.5] radians
        Normalised Range: [-1, 1] 

    headingError: Angle between roads center line and body of car in radians
        Raw Range [-pi, pi] radians
        Normalised Range: [-1, 1] 

    lateralOffset: Distance between car and road center line in meters
        Raw Range [-6, 6] m
        Normalised Range: [-1, 1]
        >= 1 Out of track

    halfWidth: Distance left and right boundary and road center line in meters
        Raw Range [-6, 6] m
        Normalised Range: [-1, 1]
        >= 1 Out of track

    rays: Seven ray shot out at -90, -45,-20, 0, 20, 45, 90 degrees and 
        distance at which they collide with enemy or obstacle capped at 50 meter

        Raw Range [0 50] m
        Normalised Range: [0, 1]
        Max 50 meter

        - angles are to left of car 
        + angles are to right of car
    
    curvatureOfRoad: Angle / meter denoting how much road is turning 20 m ahead of car per meter
        Raw Range [-0.1 0.1] radian / meter
        Normalised Range: [0, 1]

    opponentGapInMeter: Distance between car and oppponnet in meter
        Raw Range [None 50] m
        Max 50 m
        
        Normalised Range [0, 1]
        Max 1 which denotes no car detected

    opponentClosingSpeed: Difference between speed of car and speed of opponenet car
        Raw Range [-15, 15] m/s
        Normalised Range [-1, 1] 

        0 if none

        + if car is faster
        - if opponennt car is faster


    timeToCollide: In how much time out car will collide with other car in seconds
        0 if none

    """

    speed: float
    steer: float
    headingError: float
    lateralOffset: float
    halfWidth: float
    rays: np.array[float]
    curvatureOfRoad: float
    opponentGapInMeter: float | None
    opponentClosingSpeed: float
    timeToCollide: float
