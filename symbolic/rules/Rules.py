from Rule import Rule
from common.domain.domain.SensorReading import SensorReading
from symbolic.facts.Facts import Fact
from symbolic.rules.Decision import Decision
from symbolic.rules.Strategy import Startegy
from symbolic.rules.RuleConstant import *

def RecoveryAction(fact: Fact, sensorReading: SensorReading) -> Decision: 
    decision = Decision()
    decision.throttleMax = 0.3
    decision.steerBias = -k_p * (sensorReading.lateralOffset / sensorReading.halfWidth) - k_d * sensorReading.headingError

    if sensorReading.speed > 5.0:
        decision.brakeMin = 0.2

    return decision

Recovery = Rule(
    id = "R1 Recovery",
    priority = 100,
    condition = lambda fact, _: fact.outsideTrack,
    action = RecoveryAction
)

def EmergencyBrakeAction(_: Fact, sensorReading: SensorReading) -> Decision: 
    decision = Decision()

    decision.throttleMax = 0.0
    decision.brakeMin = 0.8

    return decision

EmergencyBrake = Rule(
    id = "R2 EmergencyBrake",
    priority = 95,
    condition = lambda fact, sensorReading: fact.obstacleClose and sensorReading.speed > 6.0,
    action = EmergencyBrakeAction
)

Rules = [
    Recovery,
    EmergencyBrake   
]