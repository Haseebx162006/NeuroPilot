from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule


StallRecovery = Rule(
    id = "R13 StallRecovery",
    priority = 15,
    condition = lambda fact, sensor, action: fact.stalled and fact.clearRoad,
    action = lambda fact, sensor: Decision(throttleMin = 0.6)
)