from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule


AntiTimidity = Rule(
    id = "R12 AntiTimidity",
    priority = 20,
    condition = lambda fact, sensor, action: fact.clearRoad and fact.speedLow,
    action = lambda fact, sensor: Decision(throttleMin = 0.5)
)