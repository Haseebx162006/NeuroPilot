from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule


CornerEntry = Rule(
    id = "R11 CornerEntry",
    priority = 40,
    condition = lambda fact, sensor, action: fact.cornerAhead and fact.speedHigh and not fact.sharpTurn,
    action = lambda fact, sensor: Decision(brakeMin = 0.15)
)