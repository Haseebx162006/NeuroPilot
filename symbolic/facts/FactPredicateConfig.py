from common.domain.domain.SensorReading import SensorReading
from Facts import Fact
from FactConfig import FactConfig
from math import sqrt
from common.domain.constants import HALF_TRACK_WIDTH

def resolveFacts(sensorReading: SensorReading) -> Fact:
    factConfig = FactConfig.readConfig()
    fact = Fact()

    if (sensorReading.speed > factConfig.HighSpeedThershold):
        fact.speedHigh = True

    if (sensorReading.speed < factConfig.LowSpeedThreshold):
        fact.speedLow = True

    if (abs(sensorReading.curvatureOfRoad) > factConfig.CornerAheadCurvatureThreshold):
        fact.cornerAhead = True

    if (abs(sensorReading.curvatureOfRoad) > factConfig.SharpTurnCurvatureThreshold):
        fact.sharpTurn = True

    try:
        if (sensorReading.speed > factConfig.OverspeedSafetyMargin * sqrt(factConfig.OverspeedMaxLateralAcceleration / abs(sensorReading.curvatureOfRoad))):
            fact.overspeedForCorner = True
    except ZeroDivisionError:
        fact.overspeedForCorner = False

    if (abs(sensorReading.lateralOffset) >  HALF_TRACK_WIDTH - factConfig.NearEdgeThreshold):
        fact.nearEdge = True

    if (abs(sensorReading.lateralOffset) > HALF_TRACK_WIDTH):
        fact.outsideTrack = True

    if (fact.nearEdge and (sensorReading.headingError * sensorReading.lateralOffset > 0)):
        fact.driftingOutward = True 

    if (sensorReading.rays[3] < factConfig.ObstacleAheadThreshold):
        fact.obstacleAhead = True

    if (sensorReading.rays[3] < factConfig.ObstacleCloseThreshold):
        fact.obstacleClose = True

    if (sensorReading.timeToCollide < factConfig.CollisionRiskHighThreshold):
        fact.collisionRiskHigh = True

    if (sensorReading.rays[1] > factConfig.SideFreeLeftThreshold):
        fact.sideFreeLeft = True

    if (sensorReading.rays[5] > factConfig.SideFreeRightThreshold):
        fact.sideFreeRight = True

    if (sensorReading.speed < factConfig.StalledThreshold):
        fact.stalled = True

    if (abs(sensorReading.headingError) > factConfig.HeadingMisalignedThreshold):
        fact.headingMisaligned = True

    if (sensorReading.opponentGapInMeter < factConfig.OpponentNear):
        fact.opponentNear = True

    fact.clearRoad = not any(
        [
            fact.obstacleClose,
            fact.obstacleAhead,
            fact.opponentNear,
            fact.collisionRiskHigh,
            fact.nearEdge,
            fact.outsideTrack,
            fact.driftingOutward,
            fact.headingMisaligned,
            fact.overspeedForCorner,
            fact.stalled
        ]
    )

    return fact