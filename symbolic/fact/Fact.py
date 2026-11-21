from dataclasses import dataclass

@dataclass
class Fact:
    # speed > 20 m/s
    speedHigh: bool = False
    
    # speed < 8 m/s
    speedLow: bool = False
    
    # abs(curvature_ahead) > 0.02 (radius under 50 m)
    cornerAhead: bool = False
    
    # abs(curvature_ahead) > 0.04 (radius under 25 m)
    sharpTurn: bool = False
    
    # speed > 1.15 x sqrt(6 / abs(curvature_ahead))
    overspeedForCorner: bool = False
    
    # abs(lateral_offset) > half_width - 1.5 m
    nearEdge: bool = False
    
    # abs(lateral_offset) > half_width
    outsideTrack: bool = False
    
    # near_edge and heading points toward that edge
    driftingOutward: bool = False

    # center ray under 20 m
    obstacleAhead: bool = False

    # center ray under 8 m
    obstacleClose: bool = False

    # opp_gap under 15 m
    opponentNear: bool = False

    # ttc under 1.5 s
    collisionRiskHigh: bool = False

    # side_free_left the 45-degree ray on that side is over 15 m
    sideFreeLeft: bool = False

    # side_free_right the 45-degree ray on that side is over 15 m
    sideFreeRight: bool = False

    # speed under 1 m/s
    stalled: bool = False

    # abs(heading_error) > 0.6 rad
    headingMisaligned: bool = False

    # no hazard predicate is true
    clearRoad: bool = False