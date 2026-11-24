from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule
from symbolic.rule.Strategy import Strategy

def OvertakeAction(
    fact: Fact,
    sensorReading: SensorReading,
) -> Decision:
    decision = Decision()
    decision.strategy = Strategy.OVERTAKE

    if (fact.sideFreeLeft and not fact.sideFreeRight):
        # negative for left
        decision.steerBias = -0.3
    elif fact.sideFreeRight and not fact.sideFreeLeft:
        # positive for right
        decision.steerBias = 0.3
    elif fact.sideFreeLeft and fact.sideFreeRight:
        # index 1 is -45 deg left and index 5 is +45 deg right
        decision.steerBias = -0.3 if sensorReading.rays[1] >= sensorReading.rays[5] else 0.3


    return decision


Overtake = Rule(
    id = "R8 Overtake",
    priority = 60,
    condition = lambda fact, sensor, action: (
        fact.opponentNear and
        sensor.opponentClosingSpeed > 0 and
        (fact.sideFreeRight or fact.sideFreeLeft) and
        not fact.collisionRiskHigh
    ),
    proposedAction = OvertakeAction
)