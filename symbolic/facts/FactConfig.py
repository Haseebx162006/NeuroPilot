import tomllib
from dataclasses import dataclass

@dataclass
class FactConfig:
    HighSpeedThershold: float

    LowSpeedThreshold: float

    CornerAheadCurvatureThreshold: float

    SharpTurnCurvatureThreshold: float

    OverspeedSafetyMargin: float
    OverspeedMaxLateralAcceleration: float

    NearEdgeThreshold: float

    ObstacleAheadThreshold: float

    ObstacleCloseThreshold: float

    OpponentNear: float

    CollisionRiskHighThreshold: float 

    SideFreeLeftThreshold: float

    SideFreeRightThreshold: float

    StalledThreshold: float

    HeadingMisalignedThreshold: float

    @staticmethod
    def readConfig() -> FactConfig:
        with open("Config.toml") as configFile:
            config = tomllib.load(configFile)

        return FactConfig(
            HighSpeedThershold = float(config["speed_high"]["HighSpeedThershold"]),
            
            LowSpeedThreshold = float(config["speed_low"]["LowSpeedThreshold"]),
        
            CornerAheadCurvatureThreshold = float(config["corner_ahead"]["CornerAheadCurvatureThreshold"]),
        
            SharpTurnCurvatureThreshold = float(config["sharp_turn"]["SharpTurnCurvatureThreshold"]),
        
            OverspeedSafetyMargin = float(config["overspeed_for_corner"]["OverspeedSafetyMargin"]),
            OverspeedMaxLateralAcceleration = float(config["overspeed_for_corner"]["OverspeedMaxLateralAcceleration"]),
        
            NearEdgeThreshold = float(config["near_edge"]["NearEdgeThreshold"]),
        
            ObstacleAheadThreshold = float(config["obstacle_ahead"]["ObstacleAheadThreshold"]),
        
            ObstacleCloseThreshold = float(config["obstacle_close"]["ObstacleCloseThreshold"]),
        
            OpponentNear = float(config["opponent_near"]["OpponentNear"]),
        
            CollisionRiskHighThreshold = float(config["collision_risk_high"]["CollisionRiskHighThreshold"]), 
        
            SideFreeLeftThreshold = float(config["side_free_left"]["SideFreeLeftThreshold"]),
        
            SideFreeRightThreshold = float(config["side_free_right"]["SideFreeRightThreshold"]),
        
            StalledThreshold = float(config["stalled"]["StalledThreshold"]),
        
            HeadingMisalignedThreshold = float(config["heading_misaligned"]["HeadingMisalignedThreshold"]),
        )