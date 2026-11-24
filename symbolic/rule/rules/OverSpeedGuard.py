from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule
from symbolic.rule.rules.Rules import TODO, FuzzyBrakeIntensity


def OverSpeedGuardAction(
    fact: Fact,
    sensorReading: SensorReading,
    brakingFuzzyLogic: FuzzyBrakeIntensity
) -> Decision:
    decision = Decision()

    decision.throttleMax = 0.2
    decision.brakeMin = brakingFuzzyLogic(fact, sensorReading)

    return decision


OverSpeedGuard = Rule(
    id = "R5 OverSpeedGuard",
    priority = 80,
    condition = lambda fact, sensor, action: fact.overspeedForCorner,
    proposedAction = lambda fact, sensor: OverSpeedGuardAction(fact, sensor, TODO())
)