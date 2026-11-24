from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule
from symbolic.rule.rules.Rules import TODO
from symbolic.rule.Strategy import Strategy, FuzzyCollisionRisk


def CollionAvoidanceAction(
    fact: Fact,
    sensorReading: SensorReading,
    brakingFuzzyLogic: FuzzyCollisionRisk
) -> Decision:
    decision = Decision()

    decision.throttleMax = 0.2
    decision.brakeMin = brakingFuzzyLogic(fact, sensorReading)
    decision.strategy = Strategy.EVADE

    if (fact.sideFreeLeft and not fact.sideFreeRight):
        # negative for left
        decision.steerBias = -0.4
    elif fact.sideFreeRight and not fact.sideFreeLeft:
        # positive for right
        decision.steerBias = 0.4
    elif fact.sideFreeLeft and fact.sideFreeRight:
        # index 1 is -45 deg left and index 5 is +45 deg right
        decision.steerBias = -0.4 if sensorReading.rays[1] >= sensorReading.rays[5] else 0.4


    return decision


CollionAvoidance = Rule(
    id = "R3 CollionAvoidance",
    priority = 90,
    condition = lambda fact, sensor, action: fact.opponentNear and fact.collisionRiskHigh,
    action = lambda fact, sensor: CollionAvoidanceAction(fact, sensor, TODO())
)