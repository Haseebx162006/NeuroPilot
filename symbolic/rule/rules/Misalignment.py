from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule


Misalignment = Rule(
    id = "R10 Misalignment",
    priority = 45,
    condition = lambda fact, sensor, action: fact.headingMisaligned and fact.speedHigh,
    action = lambda fact, sensor: Decision(throttleMax = 0.5)
)