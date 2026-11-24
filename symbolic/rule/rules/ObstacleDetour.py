from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule
from symbolic.rule.rules.Rules import TODO, AStartWayPintSteerBias


def ObstacleDetourAction(
    fact: Fact,
    sensorReading: SensorReading,
    steeringFuzzyLogic: AStartWayPintSteerBias
) -> Decision:
    decision = Decision()

    decision.steerBias = steeringFuzzyLogic(fact, sensorReading)

    return decision


ObstacleDetour = Rule(
    id = "R7 ObstacleDetour",
    priority = 65,
    condition = lambda fact, sensor, action: fact.obstacleAhead and not fact.obstacleClose,
    action = lambda fact, sensor: ObstacleDetourAction(fact, sensor, TODO())
)