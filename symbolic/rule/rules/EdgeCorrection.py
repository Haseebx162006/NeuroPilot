from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule

def EdgeCorrectionAction(
    fact: Fact,
    sensorReading: SensorReading,
) -> Decision:
    decision = Decision()

    if sensorReading.lateralOffset < 0:
        decision.steerBias = 0.3
    elif sensorReading.lateralOffset > 0:
        decision.steerBias = -0.3

    return decision


EdgeCorrection = Rule(
    id = "R6 EdgeCorrection",
    priority = 70,
    condition = lambda fact, sensor, action: fact.nearEdge and fact.driftingOutward,
    action = EdgeCorrectionAction
)