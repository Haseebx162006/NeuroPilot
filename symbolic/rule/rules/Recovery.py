from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.Rule import Rule
from symbolic.rule.Decision import Decision
from symbolic.rule.RuleConstant import k_d, k_p
from symbolic.rule.Strategy import Strategy


def RecoveryAction(fact: Fact, sensorReading: SensorReading) -> Decision:
    decision = Decision()
    decision.strategy = Strategy.RECOVER
    decision.throttleMax = 0.3
    decision.steerBias = -k_p * (sensorReading.lateralOffset / sensorReading.halfWidth) - k_d * sensorReading.headingError
    decision.steerBias = min(1,0, max(0.0, decision.steerBias))


    if sensorReading.speed > 5.0:
        decision.brakeMin = 0.2

    return decision

Recovery = Rule(
    id = "R1 Recovery",
    priority = 100,
    condition = lambda fact, sensor, action: fact.outsideTrack,
    action = RecoveryAction
)