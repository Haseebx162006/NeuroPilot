from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule
from symbolic.rule.rules.Rules import TODO, FuzzyBrakeIntensity


def CornerBrakingAction(
    fact: Fact,
    sensorReading: SensorReading,
    brakingFuzzyLogic: FuzzyBrakeIntensity
) -> Decision:
    decision = Decision()

    decision.throttleMax = 0.0
    decision.brakeMin = brakingFuzzyLogic(fact, sensorReading)

    return decision


CornerBraking = Rule(
    id = "R4 CornerBraking",
    priority = 85,
    condition = lambda fact, sensor, action: fact.sharpTurn and fact.speedHigh,
    action = lambda fact, sensor: CornerBrakingAction(fact, sensor, TODO())
)